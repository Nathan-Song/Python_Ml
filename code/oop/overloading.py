from functools import singledispatch

# --functools per Type


@singledispatch
def get_type(arg):
    print("This is the default type:", arg)


@get_type.register(str)
def _(arg):
    print("This is a string", arg)


@get_type.register(int)
def _(arg):
    print("This is an integer", arg)


get_type(None)
get_type("Hello World!")
get_type(100)


# -- flexible parameters
class MathLib():
    def add(self, *args):
        return sum(args)


ml = MathLib()
print(ml.add(1))
print(ml.add(1, 2))
print(ml.add(1, 2, 3))
