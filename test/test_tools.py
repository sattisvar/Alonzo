from tools import flip, noflip, aritylambda

def test_flip():
    def myf(x, y):
        return x - y

    assert myf(3, 5) == -flip(myf)(3, 5)

def test_noflip():
    def myf(x, y):
        return x - y

    assert myf(3, 5) == noflip(myf)(3, 5)

