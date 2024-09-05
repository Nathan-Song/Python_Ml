class Animal():

    def __init__(self, family):
        self.family = family

    def speak():
        print("hi I'm an animal")


class Bird(Animal):

    def __init__(self, name):
        self.name = name
        super().__init__("Birds")
        print(self.family)

    def speak(self):
        print(f"{self.family} says hiii")


bird = Bird("Elizabirth")

bird2 = Bird("Elizabirth")

bird.speak()
