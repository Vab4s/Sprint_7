SUCCESSFUL_LOGIN = r'{"id":\d+}'                                                        # 200
SUCCESSFUL_CREATION = {'ok': True}                                                      # 201

ERROR_INSUFFICIENT_CREATION_DATA = 'Недостаточно данных для создания учетной записи'    # 400
ERROR_INSUFFICIENT_LOGIN_DATA = 'Недостаточно данных для входа'                         # 400
ERROR_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'                                   # 404
ERROR_ALREADY_EXIST = 'Этот логин уже используется. Попробуйте другой.'                 # 409
