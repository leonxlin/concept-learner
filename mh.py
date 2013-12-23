
import math
import grammar

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
        proposal = proposer(samples[-1])
        if accept(samples[-1], proposal):
            samples.append(proposal)
        else:
            samples.append(samples[-1])
    return samples


def regen_proposer(grammar):
    def proposer(formula):
        if formula is None:
            return grammar.true_formula()
        formula2 = formula
        while formula2 == formula:
            formula2 = grammar.regenerate_subtree(formula)
        return formula2
    return proposer

def regen_accept(world):
    G = world.grammar
    def accept(formula, formula2):
        log_ratio = G.log_likelihood(formula2, world)\
            - G.log_likelihood(formula, world)\
            + G.log_prior(formula2) - G.log_prior(formula)\
            + math.log(formula.size_no_leaves)\
            - math.log(formula2.size_no_leaves)\
            + G.log_prob(formula) - G.log_prob(formula2)
        return math.exp(log_ratio)
    return accept
