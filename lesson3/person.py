class Person:
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека – имя, возраст"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")


man = Person("Тигран", 37)
woman = Person("Вика", 23)

man.sing()
woman.sing()
woman.dance()
