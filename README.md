# Sprint_7

Финальный проект 7 спринта — тестирование API учебного сервиса [Яндекс Самокат](https://qa-scooter.education-services.ru/).

Документация API: [qa-scooter.praktikum-services.ru/docs](https://qa-scooter.praktikum-services.ru/docs/)

## Список реализованных тестов

### 🚴 Создание курьера (`TestCreateCourier`)
Класс тестов, проверяющий создание курьера через `POST /api/v1/courier`.

| Тест | Описание |
|:---|:---|
| `test_create_courier_success_status_code` | Проверяет, что курьера можно создать и сервер возвращает код 201. |
| `test_create_courier_success_body` | Проверяет, что успешный запрос возвращает `{"ok": true}`. |
| `test_create_courier_with_existing_login_conflict` | Проверяет, что повторное создание курьера с уже существующим логином возвращает код 409 и сообщение об ошибке. |
| `test_create_courier_without_required_field_error` | **Параметризованный тест (2 кейса):** Проверяет, что отсутствие обязательного поля `login` или `password` возвращает код 400 и сообщение об ошибке. |

### 🔑 Логин курьера (`TestLoginCourier`)
Класс тестов, проверяющий авторизацию курьера через `POST /api/v1/courier/login`.

| Тест | Описание |
|:---|:---|
| `test_login_courier_success` | Проверяет, что созданный курьер может авторизоваться и сервер возвращает код 200. |
| `test_login_courier_return_id_success` | Проверяет, что успешный логин возвращает `id` курьера. |
| `test_login_courier_with_wrong_value` | **Параметризованный тест (2 кейса):** Проверяет, что неверный `login` или `password` возвращает код 404 и сообщение «Учетная запись не найдена». |
| `test_login_courier_without_required_field` | **Параметризованный тест (2 кейса):** Проверяет, что отсутствие обязательного поля `login` или `password` возвращает код 400 и сообщение «Недостаточно данных для входа». |

### 📦 Создание заказа (`TestCreateOrder`)
Класс тестов, проверяющий создание заказа через `POST /api/v1/orders`.

| Тест | Описание |
|:---|:---|
| `test_create_order_with_colors` | **Параметризованный тест (4 кейса):** Проверяет создание заказа с цветом `BLACK`, `GREY`, обоими цветами и без указания цвета. В каждом случае сервер возвращает код 201 и тело ответа содержит `track`. |

### 📋 Список заказов (`TestGetOrders`)
Класс тестов, проверяющий получение списка заказов через `GET /api/v1/orders`.

| Тест | Описание |
|:---|:---|
| `test_get_orders_list` | Проверяет, что запрос возвращает код 200 и тело ответа содержит поле `orders`. |

---

## 🛠 Технические особенности реализации

* **Структура методов:** Запросы к API вынесены в отдельные классы `CourierMethods` и `OrderMethods` в пакете `methods`.
* **Генерация данных:** Тестовые данные для курьеров и заказов генерируются с помощью библиотеки `Faker` — функции `generate_courier_data` и `generate_order_data` в `helpers.py`.
* **Параметризация:** Используется в тестах создания курьера (отсутствие обязательных полей), логина курьера (неверные значения и отсутствие полей) и создания заказа (варианты цвета).
* **Фикстуры:** В `conftest.py` определены фикстуры `courier_methods`, `order_methods` и `delete_courier` (для автоматического удаления созданных в тестах курьеров после прогона).
* **Allure-отчёт:** Все тесты размечены декораторами `@allure.suite`, `@allure.title` и `@allure.step` для генерации читаемого отчёта.

---

## 🚀 Запуск проекта

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
```bash
pytest
```

### Генерация Allure-отчёта
```bash
allure serve allure_result
```

---

## 📁 Структура проекта

```
Sprint_7/
├── methods/
│   ├── __init__.py
│   ├── courier_methods.py
│   └── order_methods.py
├── tests/
│   ├── __init__.py
│   ├── couriers/
│   │   ├── __init__.py
│   │   ├── test_create_couries.py
│   │   └── test_login_courier.py
│   └── orders/
│       ├── __init__.py
│       ├── test_create_order.py
│       └── test_get_orders.py
├── .gitignore
├── conftest.py
├── data.py
├── helpers.py
├── Makefile
├── pytest.ini
├── requirements.txt
└── README.md
```
