import requests
import random
import string
import allure
from data.urls import CREATE_COURIER


# метод генерирует строку, состоящую только из букв нижнего регистра длиной 9 символов,
# опционально в качестве параметра передаём длину строки
@allure.step('Генерация данных пользователя')
def generate_random_string(length=9):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


# 'Метод регистрации нового курьера возвращает список из логина, пароля и имени, тело ответа и код.'
# 'Если регистрация не удалась, возвращает пустой список'
@allure.step('Регистрация нового курьера')
def register_new_courier_and_return_login_password(account=None, custom_login=None, custom_password=None, custom_first_name=None):

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    if account == None:
        payload = {
            "login": login if custom_login == None else custom_login,
            "password": password if custom_password == None else custom_password,
            "firstName": first_name if custom_first_name == None else custom_first_name
        }
    else:
        payload = {
            "login": account[0],
            "password": account[1],
            "firstName": account[2]
        }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(CREATE_COURIER, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass, response.json(), response.status_code
