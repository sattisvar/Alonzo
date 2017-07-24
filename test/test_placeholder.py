from placeholder import PlaceHolder

def test_gt():
    _0 = PlaceHolder()
    _1 = PlaceHolder()
    assert (_0 > 1)(2)
    assert (1 > _0)(0)
    assert (_1 > _0)(0)(1)
    assert not (_0 > _1)(0)(1)

def test_lt():
    _0 = PlaceHolder()
    _1 = PlaceHolder()
    assert (_0 < 1)(0)
    assert (1 < _0)(2)
    assert not (_1 < _0)(0)(1)
    assert (_0 < _1)(0)(1)

def test_ge():
    _0 = PlaceHolder()
    _1 = PlaceHolder()
    assert (_0 >= 1)(2)
    assert (_0 >= 1)(1)
    assert (1 >= _0)(0)
    assert (1 >= _0)(1)
    assert (_1 >= _0)(0)(1)
    assert not (_0 >= _1)(0)(1)
    assert (_0 >= _1)(0)(0)

def test_le():
    _0 = PlaceHolder()
    _1 = PlaceHolder()
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
    _0 = PlaceHolder()
    _1 = PlaceHolder()
    assert (_0 == _1)(1)(1)
    assert not (_0 == _1)(9)(2)
    assert (_0 == 1)(1)
    assert not (_0 == 2)(1)
    assert (1 == _0)(1)
    assert not (2 == _0)(1)
