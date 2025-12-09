import pandas as pd
import random

# Generate mock data for Russian companies using CAT systems with revenue >= 100M rubles
def generate_mock_data():
    companies_data = [
        {
            'inn': '7705946271',
            'name': 'АО "Переводческие технологии"',
            'revenue': 1250000000,
            'site': 'https://translationtech.ru',
            'cat_evidence': 'найден ключевое слово: sdl trados',
            'source': 'mock_data',
            'cat_product': 'sdl trados',
            'employees': 120,
            'okved_main': '63.11'
        },
        {
            'inn': '7810004447',
            'name': 'ООО "Глобал Коннект"',
            'revenue': 850000000,
            'site': 'https://globalconnect.spb.ru',
            'cat_evidence': 'найден ключевое слово: translation memory',
            'source': 'mock_data',
            'cat_product': 'translation memory',
            'employees': 85,
            'okved_main': '74.30'
        },
        {
            'inn': '6671083633',
            'name': 'ООО "Локализация Про"',
            'revenue': 250000000,
            'site': 'https://localizationpro.ru',
            'cat_evidence': 'найден ключевое слово: memoq',
            'source': 'mock_data',
            'cat_product': 'memoq',
            'employees': 60,
            'okved_main': '62.01'
        },
        {
            'inn': '7729342181',
            'name': 'ООО "Смарткат Солюшнс"',
            'revenue': 180000000,
            'site': 'https://smartcat-solutions.ru',
            'cat_evidence': 'найден ключевое слово: smartcat',
            'source': 'mock_data',
            'cat_product': 'smartcat',
            'employees': 45,
            'okved_main': '63.11'
        },
        {
            'inn': '7704302751',
            'name': 'ООО "Мемсорс Технолоджис"',
            'revenue': 320000000,
            'site': 'https://memsource-tech.ru',
            'cat_evidence': 'найден ключевое слово: memsource',
            'source': 'mock_data',
            'cat_product': 'memsource',
            'employees': 70,
            'okved_main': '62.01'
        },
        {
            'inn': '7705744477',
            'name': 'ООО "Вордфаст Консалтинг"',
            'revenue': 150000000,
            'site': 'https://wordfast-consulting.ru',
            'cat_evidence': 'найден ключевое слово: wordfast',
            'source': 'mock_data',
            'cat_product': 'wordfast',
            'employees': 35,
            'okved_main': '74.30'
        },
        {
            'inn': '7706004897',
            'name': 'ООО "Омегат Транслейт"',
            'revenue': 110000000,
            'site': 'https://omegat-translate.ru',
            'cat_evidence': 'найден ключевое слово: omegat',
            'source': 'mock_data',
            'cat_product': 'omegat',
            'employees': 25,
            'okved_main': '74.30'
        },
        {
            'inn': '7704746761',
            'name': 'ООО "XTM Локализейшн"',
            'revenue': 210000000,
            'site': 'https://xtm-localization.ru',
            'cat_evidence': 'найден ключевое слово: xtm',
            'source': 'mock_data',
            'cat_product': 'xtm',
            'employees': 50,
            'okved_main': '63.11'
        },
        {
            'inn': '7709082530',
            'name': 'ООО "Локализе Платформа"',
            'revenue': 450000000,
            'site': 'https://lokalise-platform.ru',
            'cat_evidence': 'найден ключевое слово: lokalise',
            'source': 'mock_data',
            'cat_product': 'lokalise',
            'employees': 90,
            'okved_main': '62.01'
        },
        {
            'inn': '7705884484',
            'name': 'ООО "Краудин Солюшн"',
            'revenue': 190000000,
            'site': 'https://crowdin-solution.ru',
            'cat_evidence': 'найден ключевое слово: crowdin',
            'source': 'mock_data',
            'cat_product': 'crowdin',
            'employees': 40,
            'okved_main': '62.01'
        },
        {
            'inn': '7706281350',
            'name': 'ООО "Трансифекс Системс"',
            'revenue': 160000000,
            'site': 'https://transifex-systems.ru',
            'cat_evidence': 'найден ключевое слово: transifex',
            'source': 'mock_data',
            'cat_product': 'transifex',
            'employees': 30,
            'okved_main': '62.01'
        },
        {
            'inn': '7704145340',
            'name': 'ООО "Фрейз Технолоджи"',
            'revenue': 280000000,
            'site': 'https://phrase-technology.ru',
            'cat_evidence': 'найден ключевое слово: phrase',
            'source': 'mock_data',
            'cat_product': 'phrase',
            'employees': 55,
            'okved_main': '62.01'
        },
        {
            'inn': '7709080847',
            'name': 'ООО "Смартлинг Сервис"',
            'revenue': 350000000,
            'site': 'https://smartling-service.ru',
            'cat_evidence': 'найден ключевое слово: smartling',
            'source': 'mock_data',
            'cat_product': 'smartling',
            'employees': 75,
            'okved_main': '62.01'
        },
        {
            'inn': '7708062250',
            'name': 'ООО "ТМС Локализейшн"',
            'revenue': 220000000,
            'site': 'https://tms-localization.ru',
            'cat_evidence': 'найден ключевое слово: tms',
            'source': 'mock_data',
            'cat_product': 'tms',
            'employees': 65,
            'okved_main': '74.30'
        },
        {
            'inn': '7705836640',
            'name': 'ООО "Локализейшн Солюшнс"',
            'revenue': 140000000,
            'site': 'https://localization-solutions.ru',
            'cat_evidence': 'найден ключевое слово: локализация',
            'source': 'mock_data',
            'cat_product': None,
            'employees': 40,
            'okved_main': '63.11'
        },
        {
            'inn': '7704337341',
            'name': 'ООО "Память Переводов"',
            'revenue': 130000000,
            'site': 'https://translation-memory.ru',
            'cat_evidence': 'найден ключевое слово: память переводов',
            'source': 'mock_data',
            'cat_product': 'translation memory',
            'employees': 35,
            'okved_main': '74.30'
        },
        {
            'inn': '7706544140',
            'name': 'ООО "Терминология Про"',
            'revenue': 170000000,
            'site': 'https://terminology-pro.ru',
            'cat_evidence': 'найден ключевое слово: терминологическая база',
            'source': 'mock_data',
            'cat_product': None,
            'employees': 28,
            'okved_main': '74.30'
        },
        {
            'inn': '7704236274',
            'name': 'ООО "Переводческие Технолоджис"',
            'revenue': 200000000,
            'site': 'https://translation-tech.ru',
            'cat_evidence': 'найден ключевое слово: переводческие технологии',
            'source': 'mock_data',
            'cat_product': None,
            'employees': 50,
            'okved_main': '74.30'
        },
        {
            'inn': '7705634231',
            'name': 'ООО "Программное Обеспечение Перевода"',
            'revenue': 185000000,
            'site': 'https://translation-software.ru',
            'cat_evidence': 'найден ключевое слово: программное обеспечение для перевода',
            'source': 'mock_data',
            'cat_product': None,
            'employees': 42,
            'okved_main': '62.01'
        },
        {
            'inn': '7704835241',
            'name': 'ООО "CAT Системы Про"',
            'revenue': 260000000,
            'site': 'https://cat-systems-pro.ru',
            'cat_evidence': 'найден ключевое слово: cat',
            'source': 'mock_data',
            'cat_product': 'cat',
            'employees': 58,
            'okved_main': '62.01'
        }
    ]
    
    df = pd.DataFrame(companies_data)
    df.to_csv('data/companies.csv', index=False)
    print(f"Сгенерировано {len(df)} компаний, использующих CAT-системы с выручкой >= 100 млн руб.")
    return df

if __name__ == "__main__":
    generate_mock_data()