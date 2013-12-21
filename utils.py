
import math
from scipy.special import gammaln

def beta(alphas):
    """multinomial beta function, also the normalizing constant of the
    Dirichlet distribution"""
    return math.exp(betaln(alphas))

def betaln(alphas):
    return sum(map(gammaln, alphas)) - gammaln(sum(alphas))

