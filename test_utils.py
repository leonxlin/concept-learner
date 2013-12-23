
from utils import *

def close_enough(a, b, eps=10**-10):
    return abs(a-b) < eps

assert close_enough(beta((2,3)), 1./12)

assert close_enough(math.exp(binomln(100, 2)), 99*50)
assert close_enough(math.exp(binomln(1000, 1)), 1000)

