import requests
import allure
from data.urls import LIST_ORDER


@allure.story('Проверка списка заказов')
class TestOrder:
    @allure.title('Отображение списка заказов в теле ответа')
    def test_list_orders_in_response_body(self):
        response = requests.get(LIST_ORDER)
        assert response.status_code == 200 and 'orders' in response.text
