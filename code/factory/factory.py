class Animal():
    def speak():
        pass


class Dog(Animal):
    def speak(self):
        print("woof!")


class Cat(Animal):
    def speak(self):
        print("meow!")


class AnimalFactory():

    @staticmethod
    def new(animal_type):
        if animal_type == "dog":
            return Dog()

        elif animal_type == "cat":
            return Cat()

        return Animal()


animal_type = "dog"

AnimalFactory.new(animal_type).speak()
AnimalFactory.new(animal_type).speak()
