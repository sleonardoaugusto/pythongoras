class InvalidNumber(Exception):
    pass


def ackermann(m, n):
    if m < 0 or n < 0:
        raise InvalidNumber

    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def factorial(n):
    if n < 0:
        raise InvalidNumber

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def fibonacci(n):
    if n < 0:
        raise InvalidNumber
    if n == 0:
        return 0
    if n < 3:
        return 1

    t1 = 1
    t2 = 1
    t3 = None

    i = 2
    while i < n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3

        i += 1

    return t3
