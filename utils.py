
import math
from scipy.special import gammaln

def beta(alphas):
    """multinomial beta function, also the normalizing constant of the
    Dirichlet distribution"""
    return math.exp(betaln(alphas))

def betaln(alphas):
    return sum(map(gammaln, alphas)) - gammaln(sum(alphas))

class Memoize:
    """This code is from Jason on stackoverflow"""
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
