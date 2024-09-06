def greeting(cls):
    def greet(self):
        print("Hello, nice to meet you.")

    cls.__init__ = greet
    return cls


@greeting
class Bello:
    pass


bello = Bello()
