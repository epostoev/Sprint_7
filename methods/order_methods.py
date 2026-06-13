import allure
from data import AuthorizationData, URLS, Orders
import requests
import json


class OrderMethods:
    def __init__(self):
        self.headers = {'Authorization': AuthorizationData.tocken}
        self.url = f"{URLS.BASE_URL}"

    @allure.step("Создание заказа")
    def create_order(self, params=None):
        response = requests.post(f"{self.url}" + f"{Orders.ORDER_CREATE}",
                                 json=params
                                 )
        try:
            print(f"\n{response.json()}")
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            print(f"\n{response.text}")
            return response.text, response.status_code

    @allure.step("Получение списка заказов")
    def get_orders(self, params=None):
        response = requests.get(f"{self.url}" + f"{Orders.ORDERS_GET}",
                                json=params
                                )
        try:
            print(f"\n{response.text}")
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            print(f"\n{response.text}")
            return response.text, response.status_code
