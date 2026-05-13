from apps.models import phone_company_code


class RegisterForm:
    def __init__(self, user, confirm_password):
        self.user = user
        self.__confirm_password = confirm_password

    def __confirm_valid(self):
        if self.user.password != self.__confirm_password:
            raise Exception('confirm teng emas passwordga')

    def __password_valid(self):
        if len(self.user.password) < 4:
            raise Exception('Password uzunligi 4 dan kichik')


    def __phone_number_valid(self):
        if len(self.user.phone_number) != 9:
            raise Exception('Phone number xato')
        elif not int(self.user.phone_number[:2]) in phone_company_code:
            raise Exception('Phone number code xato')


    def user_validate(self):
        self.__confirm_valid()
        self.__password_valid()
        self.__phone_number_valid()

class LoginForm:
    def __init__(self, user):
        self.user = user



    def __is_exists(self):
        phone_number = self.user.phone_number
        password = self.user.password
        users: list = self.user.manager.objects()
        for user in users:
            if user.phone_number == phone_number:
                if user.password == password:
                    self.session_user = user
                    return
                else:
                    raise Exception('Password xato!')

        raise Exception("Account topilmadi")

    def is_login(self):
        self.__is_exists()
        return self.session_user


