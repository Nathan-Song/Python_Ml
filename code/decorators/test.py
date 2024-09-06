def tracking(cls):

    original_plus = cls.plus

    cls.__x = 0

    def new_plus(self, *args):
        self.__x += 1
        print(f"Die Methode wurde {x} Mal aufgerufen.")
        original_plus(self, *args)

    cls.plus = new_plus
    return cls


class Math():
    def kann_rechnen(self):
        print("Kann rechnen.")


@tracking
class Addition(Math):
    def plus(self, zahl):
        value = zahl + 5
        print(value)


aufgabe = Addition()
aufgabe.plus(10)
