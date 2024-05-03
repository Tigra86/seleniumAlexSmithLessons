class Person:
    """Модель человека"""

    def __init__(self, name, age, height):
        """Инициализация атрибутов человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 80
        print("Человек создан")

    def person_description(self):
        """Получение описания человека"""
        description = (self.name + ", ему " + str(self.age) + " лет, его рост " + str(self.height) + " см, его вес "
                       + str(self.weight) + " кг.")
        print("Нового человека зовут " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего человека - " + str(self.weight) + " кг.")

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создание класса Воин"""

    def __init__(self, name, age, height):
        """Инициализация атрибутов класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен " + str(self.rage))

    def person_description(self):
        """Перераспределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + " лет" + ", его заряд ярости " + str(self.rage)
        return description
