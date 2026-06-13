from data import Courier
import allure
import pytest


@allure.suite('Логин курьера')
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier_methods, delete_courier):
        with allure.step("Создать курьера"):
            courier_data, status_code, params = courier_methods.create_courier()
            delete_courier.append((params['login'], params['password']))
        with allure.step('Авторизоваться'):
            courier_data, status_code = courier_methods.get_courier(params)
        with allure.step("Проверить статус-код 200"):
            assert status_code == 200

    @allure.title("Успешый логин возвращае id")
    def test_login_courier_return_id_success(
            self, courier_methods, delete_courier):
        with allure.step("Создать курьера"):
            courier_data, status_code, params = courier_methods.create_courier()
            delete_courier.append((params['login'], params['password']))
        with allure.step('Авторизоваться'):
            courier_data, status_code = courier_methods.get_courier(params)
        with allure.step("Проверить наличе id в ответе"):
            assert courier_data.get("id") is not None

    @pytest.mark.parametrize("field, wrong_value", [
        ("login", "wrong_login"),
        ("password", "wrong_password")
    ])
    @allure.title('Неверный логин или пароль возвращает ошибку 404')
    def test_login_courier_with_wrong_value(
            self,
            courier_methods,
            delete_courier,
            field,
            wrong_value):
        with allure.step("Создать курьера"):
            courier_data, status_code, params = courier_methods.create_courier()
            delete_courier.append((params['login'], params['password']))
        with allure.step('Подменить одно из полей неверным значением'):
            login = wrong_value if field == "login" else params["login"]
            password = wrong_value if field == "password" else params["password"]
        with allure.step('Авторизоваться с неверными данными авторизации'):
            courier_data, status_code = courier_methods.get_courier(
                login, password)
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
