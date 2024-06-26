import requests
import random
import string
from data.urls import DELETE_COURIER, LOGIN


def delete_courier(userdata):
    payload = {"login": userdata[0], "password": userdata[1]}
    response = requests.post(LOGIN, data=payload)
    id = str(response.json()['id'])
    requests.delete(DELETE_COURIER + id)