import requests
import allure
from data.urls import DELETE_COURIER, LOGIN


@allure.step('Удаление курьера')
def delete_courier(userdata):
    payload = {"login": userdata[0], "password": userdata[1]}
    response = requests.post(LOGIN, data=payload)
    courier_id = str(response.json()['id'])
    requests.delete(DELETE_COURIER + courier_id)