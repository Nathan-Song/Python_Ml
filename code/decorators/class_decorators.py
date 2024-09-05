def logging(cls):
    class ChildClass(cls):

        def __init__(self, *args):
            print("A new class was created!", args)
            super().__init__(*args)

        def log():
            print("Log")

    return ChildClass

# # without decorator
# class ParentClassWithoutDec():
#     def __init__(self, name):
#         self.name = name
#         print(f"Parent Class Name = {self.name}")


# XClass = logging(ParentClassWithoutDec)
# x = XClass("XClass")


# with decorator
@logging
class ParentClass():

    def __init__(self, name):
        self.name = name
        print(f"Parent Class Name = {self.name}")

        self.log()


x = ParentClass("Paul")
