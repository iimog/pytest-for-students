import pytest

def summe(a,b):
    if type(a) is int and type(b) is int:
        return a + b
    else:
        raise TypeError("Can not calculate sum of non-ints")

def test_summe_simple():
    assert summe(3,5) == 8

def test_summe_zero():
    assert summe(0,0) == 0

def test_summe_negative():
    assert summe(1,-4) == -3

def test_summe_float():
    assert summe(.1,.5) == .6

def produkt(a,b):
    return a * b

def test_produkt_simple():
    assert produkt(2,5) == 10

def test_produkt_float():
    assert pytest.approx(produkt(0.1,0.1),0.00001) == 0.01

def quotient(a,b):
    return a / b

def test_quotien_notsosimple():
    assert quotient(5,3) == 1.666666666666666666666666666666666666666666666666666666666666666666667

def test_summe_string():
    with pytest.raises(TypeError):
        summe("a","b")

