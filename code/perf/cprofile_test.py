# import cProfile
from time import sleep


def calculate():
    result = 0

    sleep(1)

    for i in range(1, 1000):
        for i in range(1, 1000):
            result += i * i
        result += i * i

    return result

# cProfile.run("calculate()")
