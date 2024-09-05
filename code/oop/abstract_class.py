from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, abc):
        self.abc = abc

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print("wuff!")

    def move(self):
        print("My dog is running!")


# animal = Animal()

dog = Dog("abc")
print(dog.abc)
dog.make_sound()
dog.move()
