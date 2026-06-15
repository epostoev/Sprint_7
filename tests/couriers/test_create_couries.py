from data import Courier
import allure
import pytest


@allure.suite('Создание курьера')
class TestCreareCourier:
    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, courier_methods, delete_courier):
        courier_data, status_code, params = courier_methods.create_courier()
        assert (not isinstance(courier_data, str) and status_code == 201
                and courier_data.get("ok")), (
            f"{status_code}, id:{courier_data.get("ok")}")
        # input(f"\nЛОГИН = {params['login']}, ПАРОЛЬ = {params['password']}")
        delete_courier.append((params['login'], params['password']))

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_courier_with_existing_login_conflict(
            self, courier_methods, existing_courier):
        courier_data, status_code, params = courier_methods.create_courier(
            existing_courier)
        with allure.step("Повторно отпавить запрос на создание курьера с тем же логином"):
            courier_data, status_code, params = courier_methods.create_courier(
                existing_courier)
        with allure.step('Проверить, что статус-код 409 и правильное сообщение об ошибке'):
            assert (status_code == 409 and "Этот логин уже используется. Попробуйте другой." ==
                    courier_data.get("message"))

    @pytest.mark.parametrize('field', ["login", "password"])
    @allure.title('Нельзя создать курьера без поля {field}')
    def test_create_courier_without_required_field_error(
            self, courier_methods, field, delete_courier):
        with allure.step('Создать валидные данные для курьера и удалить обязательное поле'):
            courier_data = Courier.COURIER_DATA.copy()  # Создание копии словаря
            del courier_data[field]
        with allure.step('Отправить POST-запрос на создание курьера'):
            courier_data, status_code, params = courier_methods.create_courier(
                courier_data)
        with allure.step('Проверить, что статус-код 400 и правильное сообщение об ошибке'):
            assert (status_code == 400 and "Недостаточно данных для создания учетной записи" ==
                    courier_data.get("message"))
