
import math
from scipy.special import gammaln

def beta(alphas):
    """multinomial beta function, also the normalizing constant of the
    Dirichlet distribution"""
    return math.exp(betaln(alphas))

def betaln(alphas):
    return sum(map(gammaln, alphas)) - gammaln(sum(alphas))

def memoize(function):
    """Note: it kind of sucks that this isn't optimal for recursive
    functions, like fibonacci."""
    memo = {}
    def memoized(*args):
        if args not in memo:
            memo[args] = function(*args)
        return memo[args]
    return memoized
