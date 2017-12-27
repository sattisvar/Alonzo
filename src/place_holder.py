def identity_func(x):
    return x

class PlaceHolderBuilder():
    def __init__(self):
        pass

    def __getitem__(self, item_key):
        if callable(item_key):
            return PlaceHolder(0)(item_key)
        else:
            return PlaceHolder(item_key)
        
    def __call__(self):
        pass

_ = PlaceHolderBuilder()

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

    @staticmethod
    def compose_2(f):
        def _compose_2(me, other):
            if isinstance(other, PlaceHolder):
                return PlaceHolder(action=lambda *x, **y: f(me(*x, **y), other(*x, **y)), arg_name=-1)
            else:
                return PlaceHolder(action=lambda *x, **y: f(me(*x, **y), other), arg_name=me.arg_pos)
        return _compose_2
        
    def __add__(self, other):
        return self.compose_2(lambda a, b: a + b)(self, other)

    def __radd__(self, other):
        return self.compose_2(lambda a, b: b + a)(self, other)

    def __sub__(self, other):
        return self.compose_2(lambda a, b: a - b)(self, other)

    def __rsub__(self, other):
        return self.compose_2(lambda a, b: b - a)(self, other)

    def __mul__(self, other):
        return self.compose_2(lambda a, b: a * b)(self, other)

    def __rmul__(self, other):
        return self.compose_2(lambda a, b: b * a)(self, other)

    def __truediv__(self, other):
        return self.compose_2(lambda a, b: a / b)(self, other)

    def __rtruediv__(self, other):
        return self.compose_2(lambda a, b: b / a)(self, other)

    def __floordiv__(self, other):
        return self.compose_2(lambda a, b: a // b)(self, other)

    def __rfloordiv__(self, other):
        return self.compose_2(lambda a, b: b // a)(self, other)

    def __mod__(self, other):
        return self.compose_2(lambda a, b: a % b)(self, other)

    def __rmod__(self, other):
        return self.compose_2(lambda a, b: b % a)(self, other)

    def __pow__(self, other):
        return self.compose_2(lambda a, b: a ** b)(self, other)

    def __rpow__(self, other):
        return self.compose_2(lambda a, b: b ** a)(self, other)

    def __getitem__(self, other):
        return self.compose_2(lambda a, b: a[b])(self, other)

    def __eq__(self, other):
        return self.compose_2(lambda a, b: a == b)(self, other)

    def __le__(self, other):
        return self.compose_2(lambda a, b: a <= b)(self, other)

    def __lt__(self, other):
        return self.compose_2(lambda a, b: a < b)(self, other)

    def __ge__(self, other):
        return self.compose_2(lambda a, b: a >= b)(self, other)

    def __gt__(self, other):
        return self.compose_2(lambda a, b: a > b)(self, other)

