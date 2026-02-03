# 🏗 Архитектурные решения проекта "Уездный Кондитер"

## 📐 Общая архитектура

Проект реализован в виде монорепозитория с мультитенантной архитектурой и микросервисной структурой. Основные компоненты:

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   Frontend      │    │    Backend       │    │ Python Service   │
│   (React)       │◄──►│   (NestJS)       │◄──►│   (FastAPI)      │
│                 │    │                  │    │                  │
│ - Marketplace   │    │ - Tenants        │    │ - Cost Calc.     │
│ - Tenant Shop   │    │ - Shops          │    │ - Nutrition      │
│ - Constructor   │    │ - Products       │    │ - Pricing        │
│ - Checkout      │    │ - Orders         │    │ - Taxes          │
└─────────────────┘    │ - Payments       │    └──────────────────┘
                       │ - Delivery       │
                       │ - Analytics      │
                       └──────────────────┘
                                │
                       ┌──────────────────┐
                       │  Shared Services │
                       │                  │
                       │ - Database       │
                       │ - Cache (Redis)  │
                       │ - Search (ES)    │
                       │ - Storage        │
                       │ - Messaging      │
                       └──────────────────┘
```

## 🏗 Мультитенантная архитектура

### Подход к изоляции данных
- **Разделение по схемам**: Каждый тенант имеет свою схему в БД
- **Общая таблица с фильтрацией**: Использование tenant_id для разделения данных
- **Сессионная изоляция**: Контекст тенанта в каждом запросе

### Стратегия поддоменов
- Каждый магазин кондитера доступен по поддомену: `{shop-name}.uyezdny-konditer.ru`
- Единая точка входа с маршрутизацией на основе заголовков/домена
- Общая аутентификация с разграничением доступа

## 🔄 Event-Driven Architecture

### Система событий
- Используется EventBus для асинхронной коммуникации между сервисами
- События публикуются через EventEmitter2 в NestJS
- События сохраняются для аудита и восстановления

### Примеры ключевых событий
```
- TenantCreatedEvent
- OrderPlacedEvent
- PaymentProcessedEvent
- DeliveryScheduledEvent
- InventoryUpdatedEvent
- CakeConstructedEvent
```

## 📦 Микросервисы

### 1. Frontend Service
- **Технологии**: React 18, TypeScript, Vite, TailwindCSS
- **Ответственность**: UI/UX, клиентская логика, маршрутизация
- **Функции**:
  - Главный маркетплейс
  - Магазины тенантов (через поддомены)
  - Конструктор тортов (3D визуализация)
  - Корзина и оформление заказа
  - Личный кабинет

### 2. Backend Service (Core)
- **Технологии**: NestJS, TypeScript, PostgreSQL, Redis
- **Ответственность**: Бизнес-логика, API, интеграции
- **Модули**:
  - Authentication & Authorization
  - Tenant Management
  - Shop Management
  - Product Catalog
  - Cake Constructor API
  - Order Processing
  - Payment Integration
  - Delivery Management
  - Analytics & Reporting

### 3. Python Calculation Service
- **Технологии**: FastAPI, Python, NumPy, Pandas
- **Ответственность**: Вычислительная логика
- **Функции**:
  - Расчет стоимости тортов
  - Расчет пищевой ценности
  - Алгоритмы ценообразования
  - Налоговые вычисления

## 📚 Domain-Driven Design (DDD)

### Структура модулей
```
backend/src/modules/
├── auth/
├── tenants/
├── shops/
├── products/
├── cake-constructor/
├── orders/
├── payments/
├── wholesale/
├── delivery/
├── analytics/
└── notifications/
```

### Уровни DDD
1. **Domain Layer**:
   - Entities (Tenant, Shop, Product, Order)
   - Value Objects (Price, Address, ContactInfo)
   - Aggregates (ShopAggregate, OrderAggregate)
   - Domain Events (OrderCreatedEvent)

2. **Application Layer**:
   - Application Services
   - Commands & Queries
   - Command Handlers
   - Query Handlers

3. **Infrastructure Layer**:
   - Repositories Implementation
   - External Services Adapters
   - Persistence Layer

## 🔄 CQRS (Command Query Responsibility Segregation)

### Архитектура запросов
- Commands: изменение состояния системы
- Queries: получение данных
- Separate Models: разные модели для чтения и записи

### Пример структуры
```
src/
├── application/
│   ├── commands/
│   │   ├── create-tenant.command.ts
│   │   └── update-shop.command.ts
│   ├── queries/
│   │   ├── get-tenant.query.ts
│   │   └── get-products.query.ts
│   ├── command-handlers/
│   ├── query-handlers/
│   └── dtos/
├── domain/
│   ├── entities/
│   ├── value-objects/
│   └── events/
└── infrastructure/
    ├── repositories/
    └── persistence/
```

## 🔐 Безопасность

### Аутентификация и авторизация
- JWT токены с refresh механизмом
- Ролевая модель (tenant_owner, shop_manager, customer)
- Проверка прав на уровне каждого запроса
- Мiddleware для tenant isolation

### Защита данных
- Шифрование чувствительных данных
- Валидация всех входящих данных
- Защита от SQL-injection, XSS, CSRF
- Логирование безопасности

## 🗄 База данных

### Архитектура хранения
- **PostgreSQL**: основная OLTP база данных
- **Redis**: кеширование и сессии
- **Elasticsearch**: полнотекстовый поиск
- **Supabase**: аутентификация и хранение файлов

### Схема мультитенантности
- Общие таблицы: users, tenants, subscriptions
- Разделенные таблицы: shops, products, orders (с tenant_id)
- Возможность изоляции через схемы PostgreSQL

## 🚀 Инфраструктура

### Docker & Orchestration
- Контейнеризация всех сервисов
- Docker Compose для локальной разработки
- Kubernetes для продакшена
- Автомасштабирование по нагрузке

### CI/CD Pipeline
- GitHub Actions для автоматизации
- Тестирование на каждом коммите
- Автоматический деплой в staging/prod
- Rollback в случае проблем

### Мониторинг
- Prometheus для сбора метрик
- Grafana для визуализации
- Loki для логирования
- AlertManager для уведомлений

## 🧪 Тестирование

### Уровни тестирования
1. **Unit Tests**: модульное тестирование бизнес-логики
2. **Integration Tests**: интеграционные тесты с БД и внешними сервисами
3. **E2E Tests**: сквозное тестирование пользовательских сценариев
4. **Load Tests**: нагрузочное тестирование

### Тестирование мультитенантности
- Проверка изоляции данных между тенантами
- Тестирование поддоменной маршрутизации
- Проверка прав доступа

## 📱 Технические ограничения и принятые решения

### Масштабируемость
- Горизонтальное масштабирование сервисов
- Шардинг БД при необходимости
- Кеширование на уровне приложения

### Производительность
- Оптимизация запросов к БД
- Кеширование часто используемых данных
- Асинхронная обработка тяжелых операций

### Безопасность
- Использование HTTPS повсеместно
- Защита от атак на уровень аутентификации
- Регулярные аудиты безопасности

## 🔄 Обновления и обслуживание

### Стратегия обновлений
- Поэтапное развертывание новых версий
- Возможность отката к предыдущей версии
- Обслуживание без простоя (rolling updates)

### Резервное копирование
- Регулярные бэкапы БД
- Хранение бэкапов в нескольких регионах
- Автоматическое восстановление