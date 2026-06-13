import pytest
from data import Courier,URLS
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture
def courier_methods():
    return CourierMethods(url=f"{URLS.BASE_URL}{Courier.COURIER_REG}")

@pytest.fixture
def delete_courier(courier_methods):
    create_credentials = []
    yield create_credentials
    for login, password in create_credentials:
        body, status = courier_methods.get_courier({"login": login, "password": password})
        if status == 200:
            courier_id = body.get('id')
            if courier_id:
                courier_methods.delete_courier(courier_id)

@pytest.fixture
def order_methods():
    return OrderMethods()
