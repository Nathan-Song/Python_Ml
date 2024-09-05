
from collections.abc import Iterable


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self) -> str:
    #     return f"My name is {self.name} and I'm {self.age} y/0"

    def get_len():
        return 1

    def add_other_name(self, other_person):
        return Person(self.name + " " + other_person.name, 1)

    def __str__(self) -> str:
        return str({
            "name": self.name,
            "age": self.age
        })

    def __len__(self):
        return 1

    # def __add__(self, other_person):
    #     # logic goes here
    #     return self.age + other_person.age

    def __add__(self, other_person):
        # logic goes here
        return Person(self.name + " " + other_person.name, 1)

    def __dir__(self) -> Iterable[str]:
        pass

    def __gt__(self, other_person):

        return self.age > other_person.age

    __secret_dict = dict({
        'secret_name': "Test",
        "public_name": "Public Name"
    })


alice = Person("Alice", 30)
bob = Person("Bob", 15)


child2 = alice.add_other_name(bob)
child2 = alice + bob


print(alice.public_name)

print(alice)

child = alice + bob
grand_child = child + Person("Max", 18)

print(str(grand_child))

print(str(alice))
