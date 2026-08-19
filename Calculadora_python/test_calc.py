import pytest

from calculadora import soma, subtracao, multiplicacao, divisao


def test_soma():
    assert soma(10, 5) == 15


def test_subtracao():
    assert subtracao(10, 5) == 5


def test_multiplicacao():
    assert multiplicacao(10, 5) == 50


def test_divisao():
    assert divisao(10, 5) == 2


def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)


def test_soma():
    assert soma(2, 3) == 5


def test_subtracao():
    assert subtracao(5, 3) == 2


def test_multiplicacao():
    assert multiplicacao(2, 3) == 6


def test_divisao():
    assert divisao(6, 3) == 2

