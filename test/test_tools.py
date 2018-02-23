from tools import flip, noflip, aritylambda, valuefunc


def test_flip():
    def myf(x, y):
        return x - y

    assert myf(3, 5) == -flip(myf)(3, 5)


def test_noflip():
    def myf(x, y):
        return x - y

    assert myf(3, 5) == noflip(myf)(3, 5)


def test_aritylambda_n_0():
    alf = aritylambda(0, lambda x: x + 1)
    assert alf(5) == 6


def test_aritylambda_n_1():
    alf = aritylambda(1, lambda x, y: x + y)
    assert alf(5)(6) == 11
    assert alf()(4, 4) == 8


def test_aritylambda_n_2():
    alf = aritylambda(2, lambda x, y, z: x + y + z)(5, 6)
    assert alf(1) == 12


def test_valuefunc_arity_0():
    vf = valuefunc(1)
    assert vf(1) == 1
    assert vf(1, 2) == 1


def test_valuefunc_arity_1():
    vf = valuefunc(2)
    assert vf(1)(2) == 2
    assert vf(1, 2) == 2
