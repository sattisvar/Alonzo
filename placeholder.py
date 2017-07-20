from tools import flip, noflip, aritylambda

def myf(*args):
    return args

assert aritylambda(5, myf)(1)(2)(3)(4)(5) == (1, 2, 3, 4, 5)

class PlaceHolder:
    max_index = 0

    def __init__(self, index=None, result=lambda x: x, arity=1):
        self.result = result
        self.arity = arity
        self.index = index or PlaceHolder.max_index
        if index is None:
            PlaceHolder.max_index += 1

    def __call__(self, *args):
        return self.result(*args)

    def compose(self, other, f):
        if isinstance(other, PlaceHolder):
            if self.index < other.index:
                left, right, flipper = self, other, noflip
            else:
                left, right, flipper = other, self, flip
            return PlaceHolder(index=left.index,
                               arity=left.arity + right.arity,
                               result=aritylambda(left.arity,
                                                  lambda *leftarg:
                                                      PlaceHolder(index=right.index,
                                                                  arity=right.arity,
                                                                  result=aritylambda(right.arity,
                                                                                     lambda *rightarg:
                                                                                         flipper(f)(left.result(*leftarg), right.result(*rightarg))))))
        else:
            return PlaceHolder(index=self.index, arity=self.arity, result=aritylambda(self.arity, lambda *argsx: f(self.result(*argsx), other)))

    def __getitem__(self, other):
        return self.compose(other, lambda x, y: x[y])
    
    def __eq__(self, other):
        return self.compose(other, lambda x, y: x == y)

    def __le__(self, other):
        return self.compose(other, lambda x, y: x <= y)

    def __lt__(self, other):
        return self.compose(other, lambda x, y: x < y)

    def __ge__(self, other):
        return self.compose(other, lambda x, y: x >= y)

    def __gt__(self, other):
        return self.compose(other, lambda x, y: x > y)

    def __add__(self, other):
        return self.compose(other, lambda x, y: x + y)
    
    def __radd__(self, other):
        return self.compose(other, lambda x, y: y + x)

    def __sub__(self, other):
        return self.compose(other, lambda x, y: x - y)
    
    def __rsub__(self, other):
        return self.compose(other, lambda x, y: y - x)

    def __mul__(self, other):
        return self.compose(other, lambda x, y: x * y)
    
    def __rmul__(self, other):
        return self.compose(other, lambda x, y: y * x)

    def __truediv__(self, other):
        return self.compose(other, lambda x, y: x / y)
    
    def __rtruediv__(self, other):
        return self.compose(other, lambda x, y: y / x)

# assert (_0[0])([1, 2]) == 1
# assert ([1, 2][_0])(0) == 1

# # assert not (_0 > _1)(0)(1)

# if False:

#     assert (_0 == _1)(1)(1)
#     assert not (_0 == _1)(9)(2)
#     assert (_0 == 1)(1)
#     assert not (_0 == 2)(1)
#     assert (1 == _1)(1)
#     assert not (2 == _1)(1)

#     assert (_1 + 1)(1) == 2
#     assert (1 + _1)(1) == 2
#     assert (_1 + _0)(1)(2) == 3

#     assert (_1 - 1)(1) == 0
#     assert (1 - _1)(1) == 0
#     assert (_1 - _0)(1)(2) == 1
#     assert (_0 - _1)(1)(2) == -1

#     assert (_1 * 1)(1) == 1
#     assert (1 * _1)(1) == 1
#     assert (_1 * _0)(1)(2) == 2

#     assert (_1 / 2)(2) == 1
#     assert (2 / _1)(1) == 2
#     assert (_1 / _0)(2)(4) == 2
#     assert (_0 / _1)(6)(3) == 2


#     _2 = PlaceHolder()

#     assert (_0 * _1 * _2)(2)(3)(4) == 24
#     assert (_1 + _0 * _2)(4)(3)(2) == 11
#     assert (_0 + _1 * _2)(4)(3)(2) == 10
#     assert ((_0 + _1) * _2)(2)(3)(4) == 20

# print('...OK')
