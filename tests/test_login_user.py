import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User
from http import HTTPStatus

@allure.suite('Авторизация пользователя')
class Testlogin:

    @allure.description('При авторизация пользователем, который есть в системе, происходит успешная авторизация')
    @allure.title('Авторизация пользователем, который есть в системе')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_correct)
        assert response.status_code == HTTPStatus.OK.value and response.json().get('success') == True

    @allure.description('При авторизация под пользователем с некорректным логином/паролем, срабатывает allert')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_negative)
        assert response.status_code == HTTPStatus.UNAUTHORIZED.value and response.json().get('success') == False
