import timeit


def test():
    return sum(range(1000))


print(timeit.timeit("test()", globals=globals(),  number=1000))
