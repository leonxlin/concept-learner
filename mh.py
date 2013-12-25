
import math
import grammar
import random

# Metropolis-Hastings module

def mh(proposer, accept, nsamples=1000):
    """ 
    proposer(None) = a starter sample
    proposer(sample) = another sample
    accept(sample, proposal) = a boolean
    nsamples = number of samples to take
    
    mh(nsamples, proposer, accept) = list of nsamples hypotheses
    """

    samples = [proposer(None)]
    for i in xrange(nsamples - 1):
        if i%1000 == 0:
            print 'on sample', i

        proposal = proposer(samples[-1])
        if accept(samples[-1], proposal):
            samples.append(proposal)
        else:
            samples.append(samples[-1])
    return samples


