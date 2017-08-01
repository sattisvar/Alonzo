from tools import flip, noflip, aritylambda, valuefunc
from functools import partial


class PlaceHolder:
    max_index = 0

    def __init__(self, index=None, result=None, arity=None):
        if index is None:
            self.index = PlaceHolder.max_index
            PlaceHolder.max_index += 1
        else:
            self.index = index
        if arity is not None:
            self.arity = arity
        elif self.index is not None:
            self.arity = self.index + 1
        else:
            self.arity = 1
        self.result = result or valuefunc(self.arity)
            
    def __call__(self, *args):
        app = []
        phs = []
        ph = 0
        for arg in args:
            if isinstance(arg, PlaceHolder):
                phs += [ph]
                app += [ lambda precf: lambda argat: lambda tph: aritylambda(tph, lambda *precarg: partial(precf(*precarg), argat(*argu))) ]
                ph += 1
            else:
                phs += [ph]
                app += [ lambda precf: lambda argat: lambda tph: aritylambda(tph, lambda *precarg: partial(precf(*precarg), argat)) ]
        to_return = self.result
        for napp, argsat, phsat in zip(app, args, phs):
            to_return = napp(to_return)(argsat)(phsat)
        return to_return()
    
    def compose(self, other, f):
        if isinstance(other, PlaceHolder):
            if self.index < other.index:
                left, right, flipper = self, other, noflip
            else:
                left, right, flipper = other, self, flip
            newarity = max(left.arity, right.arity)
            return PlaceHolder(index=left.index,
                               arity=newarity,
                               result=aritylambda(newarity,
                                                  lambda *arg: flipper(f)(left(*arg), right(*arg))))
        else:
            return PlaceHolder(index=self.index, arity=self.arity, result=lambda *arg: f(self(*arg), other))

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

    def __floordiv__(self, other):
        return self.compose(other, lambda x, y: x // y)
    
    def __rfloordiv__(self, other):
        return self.compose(other, lambda x, y: y // x)

    def __mod__(self, other):
        return self.compose(other, lambda x, y: x % y)
    
    def __rmod__(self, other):
        return self.compose(other, lambda x, y: y % x)

    def __pow__(self, other):
        return self.compose(other, lambda x, y: x ** y)
    
    def __rpow__(self, other):
        return self.compose(other, lambda x, y: y ** x)



