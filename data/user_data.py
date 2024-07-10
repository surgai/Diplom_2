from faker import Faker

class User:
    fake = Faker()
    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'Nuykin_9@yandex.ru',
        "password": "qwerty123456"}

    data_negative = {

        "email": fake.email,
        "password": fake.password}

    data_double = {
        "email": 'Nuykin_9@yandex.ru',
        "password": "qwerty123456",
        "name": "Денис"}

    data_without_email = {
        "email": '',
        "password": "qwerty123456",
        "name": "Денис"}

    data_without_password = {
        "email": 'Nuykin_9@yandex.ru',
        "password": "",
        "name": "Денис"}

    data_without_name = {
        "email": 'Nuykin_9@yandex.ru',
        "password": "qwerty123456",
        "name": ""}

    data_updated = {
        "email": 'Nuykin_9@yandex.ru',
        "password": "qwerty123456",
        "name": "ZZZZ"}
