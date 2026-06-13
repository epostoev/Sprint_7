import allure


@allure.suite('Список заказов')
class TestGetOrders:

    @allure.title('Получение списка заказов')
    def test_get_orders_list(self, order_methods):
        with allure.step('Отправить запрос на получение списка заказов'):
            body, status_code = order_methods.get_orders()

        with allure.step('Проверить статус-код 200 и в ответе есть orders'):
            assert (status_code == 200 and "orders" in body)
