import allure
from data import AuthorizationData, URLS, Courier
from helpers import generate_courier_data
import requests
import json


class CourierMethods:
    def __init__(self):
        self.headers = {'Authorization': AuthorizationData.tocken}

    @allure.step("Создание курьера")
    def create_courier(self, params=None):
        if params is None:
            params = generate_courier_data()
        response = requests.post(
            f"{URLS.BASE_URL}{Courier.COURIER_REG}",
            data=params,
            headers=self.headers
        )
        try:
            print(f"\n{response.json()}")
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            print(f"\n{response.text}")
            return response.text, response.status_code
        
    @allure.step("Авторизация курьера")
    def get_courier(self, login, password):
        response = requests.post(
            f"{URLS.BASE_URL}{Courier.COURIER_LOGIN}",
            json = {"login": login, "password": password},
            headers=self.headers
        )
        try:
            print(f"\n{response.json()}")
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            print(f"\n{response.text}")
            return response.text, response.status_code
        
    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(
            f"{URLS.BASE_URL}{Courier.COURIER_DELETE}"+f"{courier_id}"
            # headers=self.headers
        )
        try:
            print(f"\n{response.json()}")
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            print(f"\n{response.text}")
            return response.text, response.status_code

