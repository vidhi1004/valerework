def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        raise ValueError("You cannot divide any number by zero")
    else:
        return a/b
