import pytest

from calculadora import divisao

def test_divisao():
    assert divisao(10, 5) == 2


def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)


def test_divisao():
    assert divisao(6, 3) == 2