

@profile
def func():
    a = [0] * 10
    b = [0] * 1000
    c = [0] * 10000000
    return a, b, c


def func1(x, y, z):
    first = x ** y ** z
    return first

func()
