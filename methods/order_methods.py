import allure
from data import AuthorizationData, URLS, Courier


class CourierMethods:
    def __init__(self):
        self.headers = {'Authorization': AuthorizationData.tocken}

    @allure.step("Создание курьера")
    def create_couier(self, params=None):
