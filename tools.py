from functools import partial, wraps

def flip(f):
    'Create a new function from the original one flipping the two first arguments'
    
    def newf(a, b):
        return f(b, a)
    return newf

def noflip(f):
    'provide the same function as the original'
    return f

def aritylambda(n, f):
    if n == 1:
        return f
    else:
        return lambda x: aritylambda(n - 1, partial(f, x))
                                                  
    
