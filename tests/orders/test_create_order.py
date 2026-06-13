import allure
import pytest

from helpers import generate_order_data


@allure.suite('Создание заказа')
class TestCreateOrder:

    @pytest.mark.parametrize('colors', [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None,
    ], ids=["black", "grey", "both_colors", "no_color"])
    @allure.title('Создание заказа с разными вариантами цвета')
    def test_create_order_with_colors(self, order_methods, colors):
        with allure.step('Собрать тело заказа'):
            params = generate_order_data(colors)

        with allure.step('Отправить запрос на создание заказа'):
            body, status_code = order_methods.create_order(params)

        with allure.step('Проверить статус-код 201'):
            assert status_code == 201 and "track" in body
