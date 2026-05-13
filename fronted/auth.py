from django.forms.widgets import Input

from apps.forms import  RegisterFor , LoginForm
from apps.models import User , Category


class Auth:
    def register(self):
        user_data = {
            "name": input("Ism"),
            "phone_number": input("Telefon nomer[+998]: "),
            "password": input("Parol: "),
        }

        confirm_password = input("Tasdiqlash parol: ")
        user = User(**user_data)
        manager = UserManager(user, confirm_password)
        manager.save()
        print(users)
        self.main()

    def main(self):
        menu = """
        ============== auth =================
                1. Register
                2. Login
                3. Exit
        """
        choice = input(menu)
        try:
            match choice:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as massage:
            print(massage)
            self.main()

    def login(self):
        auth = {
            "phone_number" : input("Phone: "),
            "password": input("Password: ")
        }

        user = User(**auth)
        session_user: 'User' = LoginForm(user).isdigit()
        Accaunt(session_user).main()


class Account:
    def __init__(self, session_user: 'User'):
        self.session_user = session_user

    def main(self, back=False):
        if not back:
            print(f"Hush kelibsiz! {self.session_user.name}")
        menu = """
            1. Panel
            2. Settings
            0. Logout
            >>>"""
        choice = input(menu)
        match choice:
            case "1":
                Panel(self.session_user).main()
            case "2":
                self.settings()
            case "0":
                self.main()

    def settings(self):
        menu = """
            1. About
            2. Edit
            3. Delete Account
            0. back 
            >>>"""
        choice = input(menu)
        match choice:
            case "1":
                self.session_user.about()
                self.settings()

            case "2":

                self.edit_profile()
            case "3":
                self.session_user.manager.delete()
                Auth().main()
            case "0":
                self.main(back=True)

    def edit_profile(self):
        fields = """
                            O'zgartiradigan field ni tanlang !!! 
                            1. Ism
                            2. Telefon raqam
                            3. parol

                            0. ortga
                            >>>"""

        choice = input(fields)
        if choice == "0":
            self.settings()
        else:

            if choice == "1":
                field = 'name'
            elif choice == "2":
                field = 'phone_number'
            elif choice == "3":
                field = "password"
            else:
                print("Xato qiymat kiritildi")
                self.settings()

            new_value = input("yangi qiymat kiriting: ")
            self.session_user: 'User' = self.session_user.manager.update({field: new_value})
            self.settings()


class Panel:
    def __init__(self, session_user: 'User'):
        self.session_user = session_user

    def main(self):
        menu = """

            1. Tur
            2. Hamma qilinadigan ishlar
            3. Qilinmagan ishlar
            4. Qilingan ishlar
            0. Ortga
            >>>"""

        choice = input(menu)
        match choice:
            case "*":
                pass
            case "1":
                CategoryPanel(self.session_user).main()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "0":
                Account(self.session_user).main(back=True)


class CategoryPanel:
    def __init__(self, session_user):
        self.session_category = None
        self.session_user = session_user

    def main(self):
        menu = """
            *. Search 🔍
            1. Add Category
            2. Categories
            0. Ortga
            >>>"""
        choice = input(menu)
        match choice:
            case "*":
                self.search()
            case "1":
                title = input("Nomi: ")
                Category(title=title).manager.save()
                self.main()
            case "2":
                self.list()
            case "0":
                Panel(self.session_user).main()

    def list(self):
        categories: list['Category'] = Category().manager.objects()
        for category in categories:
            print(f"{category.id}) {category.title}")

        category_id = int(input(">>>"))
        self.session_category = Category(id=category_id).manager.get_by_id()
        self.settings()

    def settings(self):
        menu = """
            1. category about
            2. category edit
            3. category delete
            0. ortga
            """
        choice = input(menu)
        match choice:
            case "1":
                self.session_category.about()
                self.settings()
            case "2":
                field = "title"
                new = input("Yangi nom: ")
                self.session_category = self.session_category.manager.update({field: new})
                self.settings()
            case "3":
                self.session_category.manager.delete()
                self.main()
            case "0":
                self.main()

    def search(self):
        search_data = input("Search : ")
        search_categories = Category(title=search_data).get_by_title()
        for category in search_categories:
            print(f"{category.id}) {category.title}")

        category_id = int(input(">>>"))
        self.session_category = Category(id=category_id).manager.get_by_id()
        self.settings()


