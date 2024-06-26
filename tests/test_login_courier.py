import requests
import allure
import re
from helpers.register_random_user import register_new_courier_and_return_login_password, generate_random_string
from helpers.delete_courier import delete_courier
from data.urls import *


@allure.story('Проверка авторизации курьера')
class TestLoginCourier:
    @allure.title('Создание курьера')
    @classmethod
    def setup_class(cls):
        cls.courier_data, _, _ = register_new_courier_and_return_login_password()
        cls.login, cls.password, cls.first_name = cls.courier_data

    @allure.title('Проверка авторизации курьера')
    @allure.description('Переданы все обязательные поля, Успешный запрос возвращает id в формате \'id\':999999')
    def test_login_fields_filled_with_correct_data(self):
        payload = {'login': self.login, 'password': self.password}
        print(payload)
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 200 and re.fullmatch(r'{"id":\d+}', response.text)

    @allure.title('Проверка авторизации курьера c указанием некорректного логина')
    def test_incorrect_login(self):
        payload = {'login': generate_random_string(), 'password': self.password}
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка авторизации курьера c указанием некорректного пароля')
    def test_incorrect_password(self):
        payload = {'login': self.login, 'password': generate_random_string()}
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка авторизации курьера c без логина')
    def test_login_without_login(self):
        payload = {'login': '', 'password': self.password}
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка авторизации курьера c без пароля')
    def test_login_without_password(self):
        payload = {'login': self.login, 'password': ''}
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка авторизации несуществующего курьера')
    def test_login_with_nonexistent_user(self):
        payload = {'login': generate_random_string(), 'password': generate_random_string()}
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Удаление созданного курьера')
    @classmethod
    def teardown_class(cls):
        delete_courier(cls.courier_data)
