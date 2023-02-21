import random

from data.data import Person
from faker import Faker

faker_eng = Faker('en_GB')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_eng.first_name() + " " + faker_eng.last_name(),
        first_name=faker_eng.first_name(),
        last_name=faker_eng.last_name(),
        age=random.randint(18, 90),
        salary=random.randint(50, 5000),
        department=faker_eng.job(),
        email=faker_eng.email(),
        current_address=faker_eng.address(),
        permanent_address=faker_eng.address(),
    )
