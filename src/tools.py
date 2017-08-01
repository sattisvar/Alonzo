from functools import partial, wraps

def flip(f):
    """Create a new function from the original one flipping the two first arguments
    """
    def newf(a, b):
        return f(b, a)
    return newf

def noflip(f):
    'provide the same function as the original'
    return f

def aritylambda(n, f):
    if n==0:
        return f
    def subvalfun(*x):
        if len(x) == 0:
            return f
        elif len(x) == 1:
            return aritylambda(n-1, partial(f, x[0]))
        else:
            return aritylambda(n-1, partial(f, x[0]))(*x[1:])
    return subvalfun

def valuefunc(arity):
    def sbval(*x):
        if len(x) >= arity:
            return x[arity-1]
        else:
            return valuefunc(arity-len(x))
    return sbval
