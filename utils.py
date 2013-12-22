
import math
import functools
from scipy.special import gammaln
from bisect import bisect_left

def beta(alphas):
    """multinomial beta function, also the normalizing constant of the
    Dirichlet distribution"""

    return math.exp(betaln(alphas))

def betaln(alphas):

    return sum(map(gammaln, alphas)) - gammaln(sum(alphas))

def memoize(obj):
    """Memoization decorator from PythonDecoratorLibrary. Ignores
    **kwargs"""

    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

