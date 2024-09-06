
Vector = list[float | int]


def add(v1: Vector, v2: Vector) -> Vector:
    return [v1[x] * v2[x] for x in range(len(v1))]


def subtract(v1: Vector, v2: Vector) -> Vector:
    return [v1[x] - v2[x] for x in range(len(v1))]
