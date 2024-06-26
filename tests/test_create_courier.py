import allure
from helpers.register_random_user import register_new_courier_and_return_login_password
from helpers.delete_courier import delete_courier


@allure.story('Проверка создания курьера')
class TestCreateCourier:
    @allure.title('Корректное создание курьера')
    @allure.description('Заполнены все поля')
    def test_creating_courier_all_fields_filled_with_correct_data(self):
        courier, response_text, response_code = register_new_courier_and_return_login_password()
        print(response_code, courier)
        assert response_text == {'ok': True} and response_code == 201
        delete_courier(courier)

    @allure.title('Создание дубликата курьера')
    @allure.description('Все поля заполнены данными уже созданного курьера')
    def test_creating_duplicate_courier(self):
        courier, _, _ = register_new_courier_and_return_login_password()
        new_courier, new_response_text, new_response_code = register_new_courier_and_return_login_password(account=courier[0])
        assert new_response_text['message'] == 'Этот логин уже используется. Попробуйте другой.' and new_response_code == 409
        delete_courier(courier)

    @allure.title('Создание курьера с заполнением обязательных полей')
    @allure.description('Все обязательные поля ("логин" и "пароль") заполнены')
    def test_creating_courier_with_required_fields(self):
        courier, response_text, response_code = register_new_courier_and_return_login_password(custom_first_name='')
        assert response_text == {'ok': True} and response_code == 201
        delete_courier(courier)

    @allure.title('Создание курьера без логина')
    @allure.description('Поле "логин" не заполнено')
    def test_creating_courier_with_no_login(self):
        courier, response_text, response_code = register_new_courier_and_return_login_password(custom_login='')
        assert response_text['message'] == 'Недостаточно данных для создания учетной записи' and response_code == 400

    @allure.title('Создание курьера без пароля')
    @allure.description('Поле "пароль" не заполнено')
    def test_creating_courier_with_no_password(self):
        courier, response_text, response_code = register_new_courier_and_return_login_password(custom_password='')
        assert response_text['message'] == 'Недостаточно данных для создания учетной записи' and response_code == 400

    @allure.title('Создание курьеров с одинаковыми логинами')
    @allure.description('Создаётся курьер с логином уже существующего курьера')
    def test_creating_couriers_with_same_login(self):
        courier, _, _ = register_new_courier_and_return_login_password()
        new_courier, new_response_text, new_response_code = register_new_courier_and_return_login_password(custom_login=courier[0][0])
        assert new_response_text['message'] == 'Этот логин уже используется. Попробуйте другой.' and new_response_code == 409
        delete_courier(courier)
