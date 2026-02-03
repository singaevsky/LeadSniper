# 📘 API Reference для проекта "Уездный Кондитер"

## 📋 Содержание

1. [Аутентификация](#authentication)
2. [Пользователи](#users)
3. [Тенанты](#tenants)
4. [Магазины](#shops)
5. [Продукты](#products)
6. [Конструктор тортов](#cake-constructor)
7. [Заказы](#orders)
8. [Платежи](#payments)
9. [Доставка](#delivery)
10. [Аналитика](#analytics)

---

## 🔐 Authentication

### POST /auth/login
Аутентификация пользователя

**Request:**
```json
{
  "email": "user@example.com",
  "password": "string"
}
```

**Response:**
```json
{
  "accessToken": "jwt_token",
  "refreshToken": "refresh_token",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "role": "customer|tenant_owner|shop_manager",
    "tenantId": "uuid"
  }
}
```

### POST /auth/register
Регистрация нового пользователя

**Request:**
```json
{
  "email": "user@example.com",
  "password": "string",
  "firstName": "string",
  "lastName": "string"
}
```

**Response:**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "firstName": "string",
  "lastName": "string"
}
```

### POST /auth/refresh
Обновление access токена

**Request:**
```json
{
  "refreshToken": "refresh_token"
}
```

**Response:**
```json
{
  "accessToken": "new_jwt_token"
}
```

---

## 👤 Users

### GET /users/profile
Получение профиля текущего пользователя

**Headers:**
```
Authorization: Bearer {token}
```

**Response:**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "firstName": "string",
  "lastName": "string",
  "phone": "string",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### PUT /users/profile
Обновление профиля пользователя

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "firstName": "string",
  "lastName": "string",
  "phone": "string"
}
```

**Response:**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "firstName": "string",
  "lastName": "string",
  "phone": "string",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

---

## 🏛️ Tenants

### POST /tenants
Создание нового тенанта (магазина кондитера)

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "name": "Название магазина",
  "subdomain": "unique-subdomain",
  "description": "Описание магазина",
  "contactInfo": {
    "phone": "+71234567890",
    "email": "contact@shop.com",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    }
  },
  "themeSettings": {
    "primaryColor": "#E63946",
    "secondaryColor": "#F1FAEE",
    "logoUrl": "https://cdn.example.com/logo.png"
  }
}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "Название магазина",
  "subdomain": "unique-subdomain",
  "description": "Описание магазина",
  "ownerId": "uuid",
  "status": "active|pending|suspended",
  "subscriptionPlan": "basic|premium|enterprise",
  "contactInfo": {
    "phone": "+71234567890",
    "email": "contact@shop.com",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    }
  },
  "themeSettings": {
    "primaryColor": "#E63946",
    "secondaryColor": "#F1FAEE",
    "logoUrl": "https://cdn.example.com/logo.png"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### GET /tenants/{id}
Получение информации о тенанте

**Headers:**
```
Authorization: Bearer {token}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "Название магазина",
  "subdomain": "unique-subdomain",
  "description": "Описание магазина",
  "ownerId": "uuid",
  "status": "active|pending|suspended",
  "subscriptionPlan": "basic|premium|enterprise",
  "contactInfo": {
    "phone": "+71234567890",
    "email": "contact@shop.com",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    }
  },
  "themeSettings": {
    "primaryColor": "#E63946",
    "secondaryColor": "#F1FAEE",
    "logoUrl": "https://cdn.example.com/logo.png"
  },
  "stats": {
    "totalProducts": 0,
    "totalOrders": 0,
    "monthlyRevenue": 0
  }
}
```

### PUT /tenants/{id}
Обновление информации о тенанте

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "name": "Новое название магазина",
  "description": "Новое описание магазина",
  "contactInfo": {
    "phone": "+71234567890",
    "email": "new-contact@shop.com",
    "address": {
      "street": "ул. Ленина",
      "building": "д. 5",
      "city": "Новый город",
      "region": "Новый регион",
      "postalCode": "654321"
    }
  },
  "themeSettings": {
    "primaryColor": "#A8DADC",
    "secondaryColor": "#1D3557",
    "logoUrl": "https://cdn.example.com/new-logo.png"
  }
}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "Новое название магазина",
  "subdomain": "unique-subdomain",
  "description": "Новое описание магазина",
  "ownerId": "uuid",
  "status": "active|pending|suspended",
  "subscriptionPlan": "basic|premium|enterprise",
  "contactInfo": {
    "phone": "+71234567890",
    "email": "new-contact@shop.com",
    "address": {
      "street": "ул. Ленина",
      "building": "д. 5",
      "city": "Новый город",
      "region": "Новый регион",
      "postalCode": "654321"
    }
  },
  "themeSettings": {
    "primaryColor": "#A8DADC",
    "secondaryColor": "#1D3557",
    "logoUrl": "https://cdn.example.com/new-logo.png"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

---

## 🏪 Shops

### GET /shops
Получение списка магазинов

**Query Parameters:**
- `limit`: integer (default: 20, max: 100)
- `offset`: integer (default: 0)
- `search`: string
- `sortBy`: string (name|createdAt|rating)
- `sortOrder`: string (asc|desc)

**Response:**
```json
{
  "data": [
    {
      "id": "uuid",
      "tenantId": "uuid",
      "name": "Название магазина",
      "description": "Описание магазина",
      "subdomain": "unique-subdomain",
      "logoUrl": "https://cdn.example.com/logo.png",
      "rating": 4.5,
      "reviewCount": 120,
      "isActive": true,
      "createdAt": "2023-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

### GET /shops/{id}
Получение информации о магазине

**Response:**
```json
{
  "id": "uuid",
  "tenantId": "uuid",
  "name": "Название магазина",
  "description": "Описание магазина",
  "subdomain": "unique-subdomain",
  "logoUrl": "https://cdn.example.com/logo.png",
  "contactInfo": {
    "phone": "+71234567890",
    "email": "contact@shop.com",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    }
  },
  "rating": 4.5,
  "reviewCount": 120,
  "stats": {
    "totalProducts": 45,
    "totalOrders": 1200,
    "monthlyRevenue": 150000
  },
  "isActive": true,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

---

## 🍰 Products

### GET /products
Получение списка продуктов

**Query Parameters:**
- `shopId`: uuid (optional)
- `category`: string (cakes|pastries|cookies|other)
- `minPrice`: number
- `maxPrice`: number
- `limit`: integer (default: 20, max: 100)
- `offset`: integer (default: 0)
- `search`: string
- `sortBy`: string (price|rating|name|createdAt)
- `sortOrder`: string (asc|desc)

**Response:**
```json
{
  "data": [
    {
      "id": "uuid",
      "shopId": "uuid",
      "name": "Название продукта",
      "description": "Описание продукта",
      "category": "cakes",
      "price": 1500.00,
      "discountPrice": 1200.00,
      "images": [
        "https://cdn.example.com/image1.jpg",
        "https://cdn.example.com/image2.jpg"
      ],
      "nutritionalInfo": {
        "calories": 350,
        "proteins": 8.5,
        "fats": 15.2,
        "carbohydrates": 45.8,
        "weight": 1000
      },
      "ingredients": [
        "мука",
        "сахар",
        "яйца",
        "сливочное масло"
      ],
      "available": true,
      "rating": 4.7,
      "reviewCount": 85,
      "createdAt": "2023-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

### GET /products/{id}
Получение информации о продукте

**Response:**
```json
{
  "id": "uuid",
  "shopId": "uuid",
  "name": "Название продукта",
  "description": "Описание продукта",
  "category": "cakes",
  "price": 1500.00,
  "discountPrice": 1200.00,
  "images": [
    "https://cdn.example.com/image1.jpg",
    "https://cdn.example.com/image2.jpg"
  ],
  "nutritionalInfo": {
    "calories": 350,
    "proteins": 8.5,
    "fats": 15.2,
    "carbohydrates": 45.8,
    "weight": 1000
  },
  "ingredients": [
    "мука",
    "сахар",
    "яйца",
    "сливочное масло"
  ],
  "customizableOptions": [
    {
      "type": "size",
      "options": [
        {
          "name": "Маленький",
          "multiplier": 0.7,
          "additionalCost": 0
        },
        {
          "name": "Средний",
          "multiplier": 1.0,
          "additionalCost": 0
        },
        {
          "name": "Большой",
          "multiplier": 1.3,
          "additionalCost": 200
        }
      ]
    }
  ],
  "available": true,
  "rating": 4.7,
  "reviewCount": 85,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

---

## 🎂 Cake Constructor

### POST /cake-constructor/calculate-price
Расчет стоимости торта по параметрам

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "baseCake": {
    "type": "biscuit|battenberg|charlotte|medovik",
    "size": {
      "diameter": 20,
      "height": 10,
      "servings": 8
    }
  },
  "layers": [
    {
      "type": "cream|jam|fruit|chocolate",
      "flavor": "vanilla|chocolate|strawberry",
      "quantity": 1
    }
  ],
  "decorations": [
    {
      "type": "berries|nuts|chocolate-ganache|fondant",
      "quantity": 1
    }
  ],
  "inscription": "С днем рождения!",
  "specialRequests": "Без сахара"
}
```

**Response:**
```json
{
  "totalPrice": 2500.00,
  "breakdown": {
    "baseCake": 1000.00,
    "layers": 800.00,
    "decorations": 500.00,
    "inscription": 100.00,
    "specialHandling": 100.00
  },
  "estimatedWeight": 1200,
  "preparationTime": 1440,
  "nutritionalInfo": {
    "calories": 420,
    "proteins": 6.5,
    "fats": 18.2,
    "carbohydrates": 58.7,
    "weight": 1200
  }
}
```

### POST /cake-constructor/create-design
Создание дизайна торта

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "name": "Мой торт",
  "description": "Персональный торт для праздника",
  "designParameters": {
    "baseCake": {
      "type": "biscuit",
      "size": {
        "diameter": 20,
        "height": 10,
        "servings": 8
      }
    },
    "layers": [
      {
        "type": "cream",
        "flavor": "vanilla",
        "quantity": 1
      }
    ],
    "decorations": [
      {
        "type": "berries",
        "quantity": 1
      }
    ],
    "colors": ["#E63946", "#F1FAEE"],
    "style": "classic|modern|children|wedding",
    "complexity": "simple|medium|complex"
  }
}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "Мой торт",
  "description": "Персональный торт для праздника",
  "userId": "uuid",
  "designParameters": {
    "baseCake": {
      "type": "biscuit",
      "size": {
        "diameter": 20,
        "height": 10,
        "servings": 8
      }
    },
    "layers": [
      {
        "type": "cream",
        "flavor": "vanilla",
        "quantity": 1
      }
    ],
    "decorations": [
      {
        "type": "berries",
        "quantity": 1
      }
    ],
    "colors": ["#E63946", "#F1FAEE"],
    "style": "classic",
    "complexity": "simple"
  },
  "thumbnailUrl": "https://cdn.example.com/cake-design-thumb.jpg",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

---

## 🛒 Orders

### POST /orders
Создание заказа

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "items": [
    {
      "productId": "uuid",
      "quantity": 1,
      "customizations": {
        "size": "large",
        "notes": "Без орехов"
      }
    }
  ],
  "deliveryInfo": {
    "type": "delivery|pickup",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "apartment": "5",
      "entrance": "1",
      "floor": "3",
      "intercom": "1234",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    },
    "preferredTime": {
      "from": "2023-01-15T14:00:00Z",
      "to": "2023-01-15T16:00:00Z"
    }
  },
  "paymentMethod": "card|cash|online",
  "comments": "Позвоните за час до доставки"
}
```

**Response:**
```json
{
  "id": "uuid",
  "userId": "uuid",
  "shopId": "uuid",
  "status": "created|confirmed|in_progress|ready|delivered|cancelled",
  "items": [
    {
      "productId": "uuid",
      "productName": "Название продукта",
      "quantity": 1,
      "price": 1500.00,
      "customizations": {
        "size": "large",
        "notes": "Без орехов"
      },
      "subtotal": 1500.00
    }
  ],
  "totalAmount": 1500.00,
  "deliveryFee": 200.00,
  "taxAmount": 210.00,
  "finalAmount": 1910.00,
  "deliveryInfo": {
    "type": "delivery",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "apartment": "5",
      "entrance": "1",
      "floor": "3",
      "intercom": "1234",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    },
    "preferredTime": {
      "from": "2023-01-15T14:00:00Z",
      "to": "2023-01-15T16:00:00Z"
    }
  },
  "paymentStatus": "pending|paid|failed",
  "paymentMethod": "card",
  "orderDate": "2023-01-10T10:00:00Z",
  "estimatedDelivery": "2023-01-15T15:00:00Z",
  "comments": "Позвоните за час до доставки"
}
```

### GET /orders/{id}
Получение информации о заказе

**Headers:**
```
Authorization: Bearer {token}
```

**Response:**
```json
{
  "id": "uuid",
  "userId": "uuid",
  "shopId": "uuid",
  "status": "confirmed",
  "items": [
    {
      "productId": "uuid",
      "productName": "Название продукта",
      "quantity": 1,
      "price": 1500.00,
      "customizations": {
        "size": "large",
        "notes": "Без орехов"
      },
      "subtotal": 1500.00
    }
  ],
  "totalAmount": 1500.00,
  "deliveryFee": 200.00,
  "taxAmount": 210.00,
  "finalAmount": 1910.00,
  "deliveryInfo": {
    "type": "delivery",
    "address": {
      "street": "ул. Пушкина",
      "building": "д. 10",
      "apartment": "5",
      "entrance": "1",
      "floor": "3",
      "intercom": "1234",
      "city": "Город",
      "region": "Регион",
      "postalCode": "123456"
    },
    "preferredTime": {
      "from": "2023-01-15T14:00:00Z",
      "to": "2023-01-15T16:00:00Z"
    }
  },
  "paymentStatus": "paid",
  "paymentMethod": "card",
  "orderDate": "2023-01-10T10:00:00Z",
  "estimatedDelivery": "2023-01-15T15:00:00Z",
  "actualDelivery": "2023-01-15T14:45:00Z",
  "comments": "Позвоните за час до доставки",
  "trackingNumber": "TK123456789",
  "deliveryStatus": "delivered"
}
```

---

## 💳 Payments

### POST /payments/process
Обработка платежа

**Headers:**
```
Authorization: Bearer {token}
```

**Request:**
```json
{
  "orderId": "uuid",
  "amount": 1910.00,
  "paymentMethod": {
    "type": "card",
    "cardToken": "tok_visa1234",
    "saveForFuture": true
  }
}
```

**Response:**
```json
{
  "id": "uuid",
  "orderId": "uuid",
  "amount": 1910.00,
  "currency": "RUB",
  "status": "succeeded|failed|pending|refunded",
  "method": "card",
  "transactionId": "txn_123456789",
  "gatewayResponse": {
    "gateway": "stripe",
    "status": "succeeded",
    "message": "Payment successful"
  },
  "processedAt": "2023-01-10T10:15:00Z"
}
```

---

## 🚚 Delivery

### GET /delivery/tracking/{orderId}
Отслеживание доставки

**Headers:**
```
Authorization: Bearer {token}
```

**Response:**
```json
{
  "orderId": "uuid",
  "status": "in_transit|delivered|returned",
  "driver": {
    "name": "Иван Петров",
    "phone": "+71234567890",
    "vehicle": "Toyota Camry, A123BC777"
  },
  "currentLocation": {
    "lat": 55.7558,
    "lng": 37.6176,
    "address": "ул. Тверская, д. 1"
  },
  "estimatedArrival": "2023-01-15T15:30:00Z",
  "deliveryHistory": [
    {
      "status": "picked_up",
      "timestamp": "2023-01-15T14:00:00Z",
      "location": "Магазин кондитера"
    },
    {
      "status": "in_transit",
      "timestamp": "2023-01-15T14:30:00Z",
      "location": "ул. Ленина, д. 5"
    }
  ]
}
```

---

## 📊 Analytics

### GET /analytics/dashboard
Получение аналитической панели

**Headers:**
```
Authorization: Bearer {token}
```

**Query Parameters:**
- `period`: string (day|week|month|quarter|year)
- `from`: string (ISO date)
- `to`: string (ISO date)

**Response:**
```json
{
  "period": {
    "from": "2023-01-01T00:00:00Z",
    "to": "2023-01-31T23:59:59Z"
  },
  "metrics": {
    "totalOrders": 150,
    "totalRevenue": 250000.00,
    "avgOrderValue": 1666.67,
    "newCustomers": 45,
    "returnRate": 25.5,
    "conversionRate": 3.2
  },
  "trends": {
    "dailyRevenue": [
      {
        "date": "2023-01-01",
        "revenue": 8000.00
      }
    ],
    "popularProducts": [
      {
        "productId": "uuid",
        "name": "Шоколадный торт",
        "salesCount": 25,
        "revenue": 37500.00
      }
    ]
  },
  "comparisons": {
    "previousPeriodGrowth": 15.5,
    "targetAchievement": 85.2
  }
}
```

## ⚙️ Общие параметры и ответы

### HTTP статусы

- `200 OK` - Запрос успешно выполнен
- `201 Created` - Ресурс успешно создан
- `400 Bad Request` - Неверный формат запроса или параметры
- `401 Unauthorized` - Необходима аутентификация
- `403 Forbidden` - Нет доступа к ресурсу
- `404 Not Found` - Ресурс не найден
- `422 Unprocessable Entity` - Валидация данных не пройдена
- `429 Too Many Requests` - Превышен лимит запросов
- `500 Internal Server Error` - Внутренняя ошибка сервера

### Формат даты
Все даты представлены в формате ISO 8601: `YYYY-MM-DDTHH:mm:ssZ`

### Ошибки

**Структура ошибки:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Поле email обязательно для заполнения",
    "details": [
      {
        "field": "email",
        "message": "Обязательное поле"
      }
    ]
  }
}
```

### Лимиты запросов
- Общее ограничение: 1000 запросов в минуту
- Для аутентифицированных пользователей: 2000 запросов в минуту
- Для администраторов: 5000 запросов в минуту