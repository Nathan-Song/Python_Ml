
def swimmable_animal(cls):
    def swim(self):
        print("This animal is swimming")

    cls.swim = swim
    return cls


class Animal():
    def make_sound(self):
        print("Make sound!")


@swimmable_animal
class Fish(Animal):
    pass


dog = Animal()
fish = Fish()
fish.swim()
# fish.make_sound()
