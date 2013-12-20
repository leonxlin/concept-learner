
import matplotlib.pyplot as plt
import random
from scipy.stats import norm
import mh

def proposer(sample):
    if sample is None:
        return 0
    return random.gauss(sample, 1)

def accept(sample, proposal):
    factor = lambda x: norm(0, 1).pdf(x) * norm(x, 1).pdf(3)
    return random.random() < factor(proposal)/factor(sample)

samples = mh.mh(proposer, accept, 10000)
plt.hist(samples, 30)
plt.show()

