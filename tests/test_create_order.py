import pytest
import allure
import requests
import re
from helpers.register_random_user import register_new_courier_and_return_login_password
from helpers.delete_courier import delete_courier
from data.endpoints import *


@allure.story('Проверка создания заказа')
class TestCreateOrder:
    @classmethod
    def setup_class(cls):
        cls.courier_data, _, _ = register_new_courier_and_return_login_password()
        cls.login, cls.password, cls.first_name = cls.courier_data

    @allure.step('Проверка возможности указания в заказе цвета самоката')
    @allure.description('Проверяется указание одного цвета отдельно, указание обоих цветов и отсутствие указания цвета')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_choose_color(self, color):
        payload = {"color": color}
        response = requests.post(CREATE_ORDER, json=payload)
        assert response.status_code == 201 and re.fullmatch(r'{"track":\d+}', response.text)

    @classmethod
    def teardown_class(cls):
        delete_courier(cls.courier_data)