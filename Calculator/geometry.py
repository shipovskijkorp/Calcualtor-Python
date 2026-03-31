def make_positive(value):
    if value < 0:
        return -value
    return value


def only_positive(value):
    if value <= 0:
        raise ValueError("Значение должно быть больше 0")
    return value


def square_perimeter(a):
    return 4 * make_positive(a)


def square_area(a):
    return make_positive(a) * make_positive(a)


def rectangle_perimeter(a, b):
    return 2 * (make_positive(a) + make_positive(b))


def rectangle_area(a, b):
    return make_positive(a) * make_positive(b)