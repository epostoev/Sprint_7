import random
import string
from data import URLS, Courier
from faker import Faker

fake = Faker()


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
    
def generate_order_data(colors = None):
    return{
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": str(fake.random_int(min=1, max=10)),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=10),
        "deliveryDate": fake.date_between(start_date="+1d", end_date="+30d").isoformat(),
        "comment": fake.text(max_nb_chars=100),
        "color": colors if colors is not None else []
    }