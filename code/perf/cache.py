from functools import lru_cache


@lru_cache
def fibonacci(n):
    print("calculated: ", n)
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(10)
fibonacci(10)
