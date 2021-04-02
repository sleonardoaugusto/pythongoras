import pytest

from mathematics import InvalidNumber, factorial


def test_invalid_number():
    with pytest.raises(InvalidNumber):
        factorial(-1)


def test_fact_1():
    assert factorial(1) == 1


def test_fact_2():
    assert factorial(2) == 2


def test_fact_3():
    assert factorial(3) == 6


def test_fact_4():
    assert factorial(4) == 24
