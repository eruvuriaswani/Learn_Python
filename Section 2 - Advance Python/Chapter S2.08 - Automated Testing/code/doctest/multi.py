def listme(x):
    """Return the square of x.
    
    this should return 4 as 2*2 = 4
    >>> listme(2)
    (2, 2)
    
    >>> listme(-2)
    (-2, -2)
    
    This will return 1
    >>> listme(-1)
    (-1, 1)
    """
    return x, x

def square(x):
    """Return the square of x.
    
    this should return 4 as 2*2 = 4
    >>> square(2)
    4
    
    >>> square(-2)
    4
    
    This will return 1
    >>> square(-1)
    2
    """

    return x * x

import doctest
doctest.testmod()
