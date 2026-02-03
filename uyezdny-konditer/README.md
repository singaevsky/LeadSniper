# 🎂 Уездный Кондитер - B2B2C Маркетплейс для кондитеров

Добро пожаловать в проект "Уездный Кондитер" - вертикальный маркетплейс для частных кондитеров и малых кондитерских.

## 🌟 Основные возможности

1. **Мультитенантная архитектура** - каждый кондитер получает собственный магазин на поддомене
2. **Конструктор тортов** - визуальный редактор для создания персонализированных тортов
3. **Оптовые закупки** - B2B2C модель для закупки ингредиентов
4. **Автоматическая доставка** - интеграция с логистическими сервисами
5. **Аналитика и отчеты** - подробная статистика продаж и спроса

## 🛠 Технологический стек

- **Frontend**: React 18 + TypeScript + Vite + TailwindCSS
- **Backend**: NestJS + TypeScript + PostgreSQL + Redis
- **Микросервис**: Python FastAPI (расчет стоимости)
- **Инфраструктура**: Docker, Kubernetes, Terraform
- **База данных**: Supabase (PostgreSQL + Auth + Storage)

## 📁 Структура проекта

```
uyezdny-konditer/
├── README.md
├── PROJECT_STRATEGY.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── docker-compose.yml
├── docs/
├── infrastructure/
├── frontend/
├── backend/
├── python-service/
├── shared/
├── supabase/
├── scripts/
└── .github/
```

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/username/uyezdny-konditer.git
cd uyezdny-konditer
```

2. Установите зависимости:
```bash
npm run install:all
```

3. Запустите проект в dev режиме:
```bash
npm run dev
```

## 📋 Документация

- [Стратегия проекта](PROJECT_STRATEGY.md)
- [Архитектурные решения](ARCHITECTURE.md)
- [Дорожная карта](ROADMAP.md)
- [Техническая документация](docs/)
- [API спецификация](docs/API-REFERENCE.md)

## 🤝 Вклад в проект

Мы приветствуем участие сообщества! Пожалуйста, ознакомьтесь с [руководством по вкладу](CONTRIBUTING.md) перед отправкой pull request.

## 📄 Лицензия

Проект распространяется под лицензией MIT.