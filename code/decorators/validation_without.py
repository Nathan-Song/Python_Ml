

class Square():
    def __init__(self, a):

        if type(a) != int and type(a) != float:
            raise ValueError("a is not an number")

        self.a = a


class Rectangle():
    def __init__(self, a, b):

        if type(a) != int and type(a) != float:
            raise ValueError("a is not an number")

        if type(b) != int and type(b) != float:
            raise ValueError("a is not an number")

        self.a = a
        self.b = b


class Triangle():
    def __init__(self, a, b, c):

        if type(a) != int and type(a) != float:
            raise ValueError("a is not an number")

        if type(b) != int and type(b) != float:
            raise ValueError("a is not an number")

        if type(c) != int and type(c) != float:
            raise ValueError("a is not an number")

        self.a = a
        self.b = b
        self.c = c


square = Square("10")
# rectangle = Rectangle("10", 5)
# triangle = Triangle(1, 2, "3")
