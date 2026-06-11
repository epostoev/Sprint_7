class AuthorizationData:
    tocken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTIxNGJlNGE1YzcxMjAwM2QwZWE4NzMiLCJpYXQiOjE3ODA1NjcwMTMsImV4cCI6MTc4MTE3MTgxM30.c92EhdUmzL1sD5yqjn9IARGReQtdrkZ6w8u_hMFCsC0'

# Тестируемый сайт
class URLS:
    BASE_URL = "https://qa-scooter.education-services.ru"

class Courier:
    COURIER_REG = "/api/v1/courier"             #POST Создание курьера
    COURIER_LOGIN = "/api/v1/courier/login"     #POST Логин курьера в системе
    COURIER_DELETE = "/api/v1/courier/"         #DELETE Удаление курьера
    COURIER_DATA = {"login": "lharysen", "password": "1234", "firstName": "Евгений"}

class Orders:
    ORDER_CREATE = "/api/v1/orders"
    ORDERS_GET = "/api/v1/orders"