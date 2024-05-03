class Car:
    def __init__(self, model, year, engine, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.mileage = mileage
        self.wheels = 4

    def car_description(self):
        description = (self.model + " " + str(self.year) + " года, объем двигателя - " + str(self.engine) +
                       " кубических метров, его пробег - " + str(self.mileage) + " км, количество колёс - ") + str(
            self.wheels)
        print("Характеристики новой машины: " + description)


class Truck(Car):
    def __init__(self, model, year, engine, mileage):
        super().__init__(model, year, engine, mileage)
        self.wheels = 8


car = Car("BMW", 2023, 8, 2000)
car.car_description()

truck = Truck("GMC", 2018, 16, 30000)
truck.car_description()


