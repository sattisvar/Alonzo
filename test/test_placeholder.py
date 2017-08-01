from placeholder import *

_0 = PlaceHolder()
_1 = PlaceHolder()
_2 = PlaceHolder()
_3 = PlaceHolder()
_4 = PlaceHolder()
_5 = PlaceHolder()
_6 = PlaceHolder()

def test_pick():
    result = _0(1)
    assert isinstance(result, int)
    assert result == 1

def test_leftover():
    result = _0(1, 2)
    assert isinstance(result, int)
    assert result == 1

def test_oneunused():
    result = _1(1, 2)
    assert isinstance(result, int)
    assert result == 2

def test_gt():
    assert (_0 > 1)(2)
    assert (1 > _0)(0)
    assert (_1 > _0)(0)(1)
    assert not (_0 > _1)(0)(1)

def test_lt():
    assert (_0 < 1)(0)
    assert (1 < _0)(2)
    assert not (_1 < _0)(0)(1)
    assert (_0 < _1)(0)(1)

def test_ge():
    assert (_0 >= 1)(2)
    assert (_0 >= 1)(1)
    assert (1 >= _0)(0)
    assert (1 >= _0)(1)
    assert (_1 >= _0)(0)(1)
    assert not (_0 >= _1)(0)(1)
    assert (_0 >= _1)(0)(0)

def test_le():
    assert (_0 <= 1)(0)
    assert (_0 <= 1)(1)
    assert (1 <= _0)(2)
    assert (1 <= _0)(1)
    assert not (_1 <= _0)(0)(1)
    assert (_1 <= _0)(1)(1)
    assert (_0 <= _1)(0)(1)

def test_add():
    _0 = PlaceHolder()
    _1 = PlaceHolder()
    assert (_0 + 1)(1) == 2
    assert (1 + _0)(1) == 2
    assert (_0 + _1)(1)(2) == 3
    
def test_eq():
    assert (_0 == _1)(1)(1)
    assert not (_0 == _1)(9)(2)
    assert (_0 == 1)(1)
    assert not (_0 == 2)(1)
    assert (1 == _0)(1)
    assert not (2 == _0)(1)

def test_add():
    assert (_0 + 1)(1) == 2
    assert (1 + _0)(1) == 2
    assert (_1 + _0)(1)(2) == 3

def test_sub():
    assert (_0 - 1)(1) == 0
    assert (1 - _0)(1) == 0
    assert (_1 - _0)(1)(2) == 1
    assert (_0 - _1)(1)(2) == -1

def test_mul():
    assert (_0 * 1)(1) == 1
    assert (1 * _0)(1) == 1
    assert (_1 * _0)(1)(2) == 2

def test_div():
    assert (_0 / 2)(2) == 1
    assert (2 / _0)(1) == 2
    assert (_1 / _0)(2)(4) == 2
    assert (_0 / _1)(6)(3) == 2

def test_floordiv():
    assert (_0 // 2)(3) == 1
    assert (2 // _0)(3) == 0
    assert (_1 // _0)(2)(5) == 2
    assert (_0 // _1)(8)(3) == 2

def test_mod():
    assert (_0 % 2)(4) == 0
    assert (4 % _0)(3) == 1
    assert (_1 % _0)(5)(7) == 2
    assert (_0 % _1)(6)(4) == 2

def test_getitem():
    assert (_0[0])([1, 2]) == 1

def test_cross():
    assert ((_0[0] + _2[0]) * (_1 + _3))([1, 2], 3, [4, 5], 6) == 45

def test_double():
    assert (_0 + _0)(10) == 20

def test_power():
    assert (_0 ** 2)(7) == 49
    assert (2 ** _0)(10) == 1024
    assert (_0 ** _1)(2, 5) == 32
    assert (_1 ** _0)(2, 5) == 25

