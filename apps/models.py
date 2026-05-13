import json
phone_company_code = [99,97,91,95,93,90,88,94,77,]
from dataclasses import dataclass


@dataclass
class Manager:
    obj: object = None

    @property
    def file_name(self):
        return self.obj.__class__.__name__.lower() + "s.json"

    @property
    def file_path(self):
        return f"/Users/user/PycharmProjects/ToDo/database/{self.file_name}"

    def write(self, objs):
        list_data = []
        for obj in objs:
            list_data.append(obj.__dict__)
        with open(self.file_path, 'w') as f:
            json.dump(list_data, f, indent=3)

    def read(self):
        file_path = self.file_path
        try:
            with open(file_path) as f:
                data = json.load(f)
        except:
            data = []
        return data

    def objects(self) -> list:
        data: list[dict] = self.read()
        objects = []
        for d in data:
            obj = self.obj.__class__(**d)
            objects.append(obj)
        return objects

    def save(self):
        objs = self.objects()
        new_id = objs[-1].id + 1 if objs else 1
        self.obj.id = new_id
        objs.append(self.obj)
        self.write(objs)

    def update(self, kwargs: dict):  # {attr1 : value , attr2 : value}
        objects = self.objects()

        for obj in objects:
            if int(obj.id) == int(self.obj.id):
                for attr_name, value in kwargs.items():
                    setattr(obj, attr_name, value)
                self.write(objects)
                return obj

    def delete(self):
        objects = self.objects()

        for obj in objects:
            if int(obj.id) == int(self.obj.id):
                objects.remove(obj)
        self.write(objects)

    def get_by_id(self):

        objs = self.objects()
        for obj in objs:
            if int(obj.id) == int(self.obj.id):
                return obj



@dataclass
class User:
    id: int = None
    name: str = None
    phone_number: str = None
    password: str = None

    @property
    def manager(self):
        return Manager(self)

    def about(self):
        text = f"""
            Ismi : {self.name}
            Telefon : {self.phone_number}
            password : {len(self.password) * "*"}
            """
        print(text)


@dataclass
class Category:
    id: int = None
    title: str = None

    @property
    def manager(self):
        return Manager(self)

    def about(self):
        text = f"""
            Nomi : {self.title}
            """
        print(text)

    def get_by_title(self):
        data = self.title.lower()
        finds = []
        categories: list['Category'] = self.manager.objects()
        for category in categories:
            if data in category.title.lower():
                finds.append(category)
        return finds


@dataclass
class Todo:
    id: int = None
    description: str = None
    datetime: str = None
    category: Category = None
    owner: User = None
    status: str = 'new'

    @property
    def manager(self):
        return Manager(self)






















