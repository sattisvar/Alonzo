import operator
from tools import flip

def identity_func(x):
    return x

def _(item_key):
    if callable(item_key):
        return PlaceHolder(0)(item_key)
    elif isinstance(item_key, str):
        return PlaceHolder(item_key)
    else:
        try:
            iterator = iter(item_key)
            return PlaceHolder(action=lambda *x, **y: item_key, arg_name=-1)
        except TypeError:
            return PlaceHolder(item_key)

class PlaceHolder():
    value = 0

    def __init__(self, arg_name=None, action=None):
        if action is None:
            self.action = identity_func
            if arg_name is None:
                self.arg_pos = PlaceHolder.value
                PlaceHolder.value += 1
            else:
                self.arg_pos = arg_name
        else:
            self.action = action
            self.arg_pos = arg_name if arg_name is not None else 0

    @staticmethod
    def reset():
        PlaceHolder.value = 0

    def __call__(self, *args, **kwargs):
        if self.arg_pos == -1:
            return self.action(*args, **kwargs)
        else:
            if isinstance(self.arg_pos, int):
                return self.action(args[self.arg_pos])
            else:
                return self.action(kwargs[self.arg_pos])

    def compose_2(self, f, other):
        if isinstance(other, PlaceHolder):
            return PlaceHolder(action=lambda *x, **y: f(self(*x, **y), other(*x, **y)), arg_name=-1)
        else:
            return PlaceHolder(action=lambda *x, **y: f(self(*x, **y), other), arg_name=self.arg_pos)

    def compose_1(self, f):
        return PlaceHolder(action=lambda *x, **y: f(self(*x, **y)), arg_name=self.arg_pos)

    def __add__(self, other):
        return self.compose_2(operator.add, other)

    def __radd__(self, other):
        return self.compose_2(flip(operator.add), other)

    def __sub__(self, other):
        return self.compose_2(operator.sub, other)

    def __rsub__(self, other):
        return self.compose_2(flip(operator.sub), other)

    def __mul__(self, other):
        return self.compose_2(operator.mul, other)

    def __rmul__(self, other):
        return self.compose_2(flip(operator.mul), other)

    def __truediv__(self, other):
        return self.compose_2(operator.truediv, other)

    def __rtruediv__(self, other):
        return self.compose_2(flip(operator.truediv), other)

    def __floordiv__(self, other):
        return self.compose_2(operator.floordiv, other)

    def __rfloordiv__(self, other):
        return self.compose_2(flip(operator.floordiv), other)

    def __mod__(self, other):
        return self.compose_2(operator.mod, other)

    def __rmod__(self, other):
        return self.compose_2(flip(operator.mod), other)

    def __pow__(self, other):
        return self.compose_2(operator.pow, other)

    def __rpow__(self, other):
        return self.compose_2(flip(operator.pow), other)

    def __getitem__(self, other):
        return self.compose_2(operator.getitem, other)

    def __eq__(self, other):
        return self.compose_2(operator.eq, other)

    def __le__(self, other):
        return self.compose_2(operator.le, other)

    def __lt__(self, other):
        return self.compose_2(operator.lt, other)

    def __ge__(self, other):
        return self.compose_2(operator.ge, other)

    def __gt__(self, other):
        return self.compose_2(operator.gt, other)

    def __ne__(self, other):
        return self.compose_2(operator.ne, other)

    def __and__(self, other):
        return self.compose_2(operator.and_, other)

    def __lshift__(self, other):
        return self.compose_2(operator.lshift, other)

    def __rshift__(self, other):
        return self.compose_2(operator.rshift, other)

    def __invert__(self):
        return self.compose_1(operator.inv)

    def __not__(self):
        return self.compose_1(operator.not_)

    def __abs__(self):
        return self.compose_1(operator.abs)

    def __bool__(self):
        return self.compose_1(operator.truth)
