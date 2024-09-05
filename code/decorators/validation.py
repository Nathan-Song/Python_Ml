def num_validation(cls):
    original_init = cls.__init__

    def validation_init(self, *args):
        for x in args:
            if type(x) != int and type(x) != float:
                raise ValueError(f"{x} is not an number")

        original_init(self, *args)

    cls.__init__ = validation_init

    return cls


@num_validation
class Square():
    def __init__(self, a):
        self.a = a
        print(f"a = {self.a}")


@num_validation
class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"a = {self.a}")
        print(f"b = {self.b}")


@num_validation
class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(f"a = {self.a}")
        print(f"b = {self.b}")
        print(f"c = {self.c}")


square = Square(10)
print("---")
rectangle = Rectangle(10, 5)
print("---")
triangle = Triangle(1, 2, 3)
