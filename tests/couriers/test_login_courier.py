from data import Courier
import allure
import pytest


@allure.suite('Логин курьера')
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier_methods, existing_courier):
        with allure.step('Авторизоваться'):
            courier_data, status_code = courier_methods.get_courier(existing_courier)
        with allure.step("Проверить статус-код 200"):
            assert status_code == 200

    @allure.title("Успешый логин возвращае id")
    def test_login_courier_return_id_success(
            self, courier_methods, existing_courier):
        with allure.step('Авторизоваться'):
            courier_data, status_code = courier_methods.get_courier(existing_courier)
        with allure.step("Проверить наличе id в ответе"):
            assert courier_data.get("id") is not None

    @allure.title('Авторизация с неверным логином возвращает ошибку 404')
    def test_login_courier_with_wrong_login(self, courier_methods, existing_courier):
        with allure.step('Авторизоваться с неверным логином'):
            courier_data, status_code = courier_methods.get_courier(
                {"login": "wrong_login", "password": existing_courier["password"]})
        with allure.step("Проверить статус-код 404 и сообщение об ошибке"):
            assert (status_code == 404 and courier_data.get(
                "message") == "Учетная запись не найдена")


    @allure.title('Авторизация с неверным паролем возвращает ошибку 404')
    def test_login_courier_with_wrong_password(self, courier_methods, existing_courier):
        with allure.step('Авторизоваться с неверным паролем'):
            courier_data, status_code = courier_methods.get_courier(
                {"login": existing_courier["login"], "password": "wrong_password"})
        with allure.step("Проверить статус-код 404 и сообщение об ошибке"):
            assert (status_code == 404 and courier_data.get(
                "message") == "Учетная запись не найдена")

    @pytest.mark.parametrize("field", [
        "login",
        "password"
    ])
    @allure.title('Авторизация без обязательного поля возвращает ошибку 400')
    def test_login_courier_without_required_filed(self, courier_methods, field):
        with allure.step('Создать валидные данные для курьера и удалить обязательное поле'):
            courier_data = Courier.COURIER_DATA.copy()  # Создание копии словаря
            del courier_data[field]
        with allure.step('Авторизоваться с неверными данными авторизации'):
            courier_data, status_code = courier_methods.get_courier(
                courier_data)
        with allure.step("Проверить статус-код 400 и сообщение об ошибке"):
            assert (status_code == 400 and courier_data.get(
                "message") == "Недостаточно данных для входа")
