import pytest
from hesap import topla, cikar, carp, bol

def test_topla():
    assert topla(2, 3) == 5
    assert topla(-1, 1) == 0
    assert topla(0, 0) == 0

def test_cikar():
    assert cikar(5, 3) == 2
    assert cikar(0, 0) == 0
    assert cikar(-1, -1) == 0   

def test_carp():
    assert carp(2, 3) == 6
    assert carp(-1, 1) == -1
    assert carp(0, 5) == 0

def test_bol():
    assert bol(6, 3) == 2
    assert bol(-4, 2) == -2
    with pytest.raises(ValueError):
        bol(5, 0)   

