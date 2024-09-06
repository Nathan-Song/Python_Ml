from typing import Union, Tuple
IS_LOADING_PROCESS = True


AdditionNumber = Union[int, float]


def greet(name: str) -> str:
    return f"Hi {name}"


def add(x: AdditionNumber, y: AdditionNumber) -> AdditionNumber:
    return x + y


Vector = list[float]


def vector_product(v1: Vector, v2: Vector) -> float:
    return sum(v1) + sum(v2)


def get_user() -> Tuple[str, int]:
    return ("Alice", 20)


print(add(1.5, 2))


def process_data(is_loading: bool) -> bool:
    '''Test'''

    if not is_loading:
        print("not loading")
    else:
        print("loading")

    return True


process_data(IS_LOADING_PROCESS)
