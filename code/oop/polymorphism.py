class Vehicle():
    tires = 1
    age: int

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} has started with {self.tires} tires!")


class MotoCycle(Vehicle):
    tires = 2
    pass


class Car(Vehicle):
    tires = 4
    pass


def start_vehicle(vehicle: Vehicle):
    vehicle.start()


testCase = 1
test_case = 2

car = Car(name="bmw",)
moto = MotoCycle("yahama")


start_vehicle(car)
start_vehicle(moto)
