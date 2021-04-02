import pytest

from mathematics import InvalidNumber, ackermann


def test_m_negative():
    with pytest.raises(InvalidNumber):
        ackermann(-1, 1)


def test_m_0():
    assert ackermann(0, 1) == 2


def test_n_0():
    assert ackermann(1, 0) == 2


def test_m_n_1():
    assert ackermann(1, 1) == 3


def test_m_n_2():
    assert ackermann(2, 2) == 7
