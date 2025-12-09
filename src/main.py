import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import os

BASE_URL = "https://www.list-org.com"

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Ошибка при запросе {url}: {response.status_code}")
    except Exception as e:
        print(f"Ошибка при запросе {url}: {e}")
    return None

def parse_company_list(html, okved):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='org_list')
    if table is None:
        return []
    rows = table.find_all('tr')
    companies = []
    for row in rows[1:]:  # пропускаем заголовок
        link = row.find('a')
        if link and link.get('href'):
            company_url = BASE_URL + link['href']
            companies.append(company_url)
    return companies

def parse_company_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Название
    name_elem = soup.find('h1', class_='org_name')
    if name_elem is None:
        name_elem = soup.find('div', class_='org_name')
    name = name_elem.text.strip() if name_elem else None

    # ИНН
    inn = None
    inn_pattern = re.compile(r'ИНН\s*(\d+)')
    inn_match = inn_pattern.search(html)
    if inn_match:
        inn = inn_match.group(1)

    # Выручка
    revenue = None
    financial_div = soup.find('div', class_='financial')
    if financial_div:
        table = financial_div.find('table')
        if table:
            rows = table.find_all('tr')
            for row in rows:
                tds = row.find_all('td')
                if len(tds) >= 3 and 'Выручка' in tds[0].text:
                    revenue_str = tds[2].text
                    # Удаляем " руб." и пробелы
                    revenue_str = revenue_str.replace(' руб.', '').replace(' ', '')
                    try:
                        revenue = int(revenue_str)
                    except:
                        pass
                    break

    # Сайт
    website = None
    # Ищем ссылку, которая ведет на внешний сайт
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('http') and 'list-org' not in href:
            website = href
            break

    # ОКВЭД
    okved_main = None
    # Ищем ОКВЭД на странице, обычно в тексте
    okved_pattern = re.compile(r'ОКВЭД\s*(\d+\.\d+(?:\.\d+)?)')
    okved_match = okved_pattern.search(html)
    if okved_match:
        okved_main = okved_match.group(1)

    # Количество сотрудников
    employees = None
    # Ищем "Среднесписочная численность"
    employees_pattern = re.compile(r'Среднесписочная численность\s*(\d+)')
    employees_match = employees_pattern.search(html)
    if employees_match:
        employees = int(employees_match.group(1))

    return {
        'name': name,
        'inn': inn,
        'revenue': revenue,
        'site': website,
        'okved_main': okved_main,
        'employees': employees
    }

def check_cat(website):
    if website is None:
        return False, None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(website, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()
            keywords = ['cat', 'translation memory', 'tms', 'локализация', 'память переводов', 'терминологическая база', 'переводческий', 'переводов', 'sdl trados', 'memoq', 'smartcat', 'memsource', 'wordfast', 'omegat', 'xtm', 'lokalise', 'crowdin', 'transifex', 'phrase', 'smartling', 'переводческие технологии', 'программное обеспечение для перевода']
            for keyword in keywords:
                if keyword in text:
                    return True, keyword
    except Exception as e:
        print(f"Ошибка при проверке сайта {website}: {e}")
    return False, None

def main():
    okveds = ['63.11', '62.01', '58.29', '74.30']
    all_companies = []

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    for okved in okveds:
        page = 1
        while True:
            url = f"{BASE_URL}/search?type=okved&val={okved}&page={page}"
            print(f"Парсинг страницы: {url}")
            html = get_page(url)
            if html is None:
                break
            company_urls = parse_company_list(html, okved)
            if not company_urls:
                break
            for company_url in company_urls:
                print(f"Парсинг компании: {company_url}")
                company_html = get_page(company_url)
                if company_html:
                    company_data = parse_company_page(company_html)
                    company_data['source'] = 'list-org'
                    all_companies.append(company_data)
                time.sleep(3)  # задержка, чтобы не нагружать сервер
            # Проверяем, есть ли следующая страница
            soup = BeautifulSoup(html, 'html.parser')
            next_page = soup.find('a', text='Далее')
            if next_page:
                page += 1
            else:
                break
            time.sleep(5)

    # Сохраняем все компании в промежуточный файл
    df_all = pd.DataFrame(all_companies)
    df_all.to_csv('data/all_companies.csv', index=False)
    print(f"Собрано {len(df_all)} компаний из источника.")

    # Фильтруем по выручке (>= 100 млн)
    df_filtered = df_all[df_all['revenue'] >= 100000000] if 'revenue' in df_all.columns and df_all['revenue'].notna().any() else pd.DataFrame()

    if df_filtered.empty:
        print("Не найдено компаний с выручкой >= 100 млн руб.")
        return

    print(f"Найдено {len(df_filtered)} компаний с выручкой >= 100 млн руб.")

    # Проверяем сайты на наличие CAT-систем
    result = []
    for idx, row in df_filtered.iterrows():
        website = row['site']
        if pd.isna(website) or website is None:
            continue
        has_cat, keyword = check_cat(website)
        if has_cat:
            row_dict = row.to_dict()
            row_dict['cat_evidence'] = f"найден ключевое слово: {keyword}"
            row_dict['cat_product'] = None  # можно уточнить по ключевому слову
            # Если ключевое слово совпадает с названием продукта, то записываем
            product_keywords = ['sdl trados', 'memoq', 'smartcat', 'memsource', 'wordfast', 'omegat', 'xtm', 'lokalise', 'crowdin', 'transifex', 'phrase', 'smartling']
            if any(prod in keyword for prod in product_keywords):
                row_dict['cat_product'] = keyword
            result.append(row_dict)
        time.sleep(5)  # задержка, чтобы не нагружать сайты

    # Сохраняем результат
    df_result = pd.DataFrame(result)
    # Выбираем только нужные столбцы
    columns = ['inn', 'name', 'revenue', 'site', 'cat_evidence', 'source', 'cat_product', 'employees', 'okved_main']
    if not df_result.empty:
        df_result = df_result[columns]
        df_result.to_csv('data/companies.csv', index=False)
        print(f"Найдено и сохранено {len(df_result)} компаний, использующих CAT-системы с выручкой >= 100 млн руб.")
    else:
        print("Не найдено компаний, соответствующих всем критериям.")
        # Create an empty file with the right structure
        empty_df = pd.DataFrame(columns=columns)
        empty_df.to_csv('data/companies.csv', index=False)

if __name__ == "__main__":
    main()