import pytest

from mathematics import InvalidNumber, fibonacci


def test_invalid_number():
    with pytest.raises(InvalidNumber):
        fibonacci(-1)


def test_n_1():
    assert fibonacci(1) == 1


def test_n_2():
    assert fibonacci(2) == 1


def test_n_3():
    assert fibonacci(3) == 2


def test_n_5():
    assert fibonacci(5) == 5


def test_n_6():
    assert fibonacci(6) == 8


def test_n_7():
    assert fibonacci(7) == 13
