import allure
from data import AuthorizationData, URLS, Courier
from helpers import generate_courier_data
import requests
import json


class CourierMethods:
    def __init__(self, url):
        self.headers = {'Authorization': AuthorizationData.tocken}
        self.url = url

    @allure.step("Создание курьера")
    def create_courier(self, params=None):
        if params is None:
            with allure.step('Создать валидные данные для курьера'):
                params = generate_courier_data()
        with allure.step('Отправить POST-запрос на создание курьера'):
            response = requests.post(
                f"{self.url}",
                data=params
            )
        try:
            return response.json(), response.status_code, params
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Авторизация курьера")
    def get_courier(self, params=None):
        response = requests.post(
            f"{URLS.BASE_URL}{Courier.COURIER_LOGIN}",
            json=params,
            headers=self.headers,
            timeout=15
        )
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(
            f"{URLS.BASE_URL}{Courier.COURIER_DELETE}" + f"{courier_id}"
            # headers=self.headers
        )
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
