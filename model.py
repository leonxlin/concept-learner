
import world
import dnf
import mh
import utils
import math
import random

class BinaryFeatureLearnerModel(object):

    def __init__(self, world, outlier_param=float('Inf'),
            rules=dnf.RULE_SETS[0]):
        """exp(-outlier_param) is the probability that an observation
        is to be discounted"""

        self.world = world
        self.outlier_param = outlier_param

        # define grammar

        def feature_decider(feat):
            return lambda obj, e: feat in obj.features
        symbols = [dnf.PredicateSymbol(str(feat),
            feature_decider(feat)) for feat in world.features]
        self.grammar = dnf.DNF(symbols, rules)

        self.samples = {} # {sample: count for each sample}

    def sample_formulas(self, n=30000):
        """Sample n formulas from the posterior using Metropolis-Hastings.
        Result is returned and stored in self.samples"""
        
        self.samples = {}

        for f in mh.mh(self._regen_proposer(), self._regen_accept(), n):
            if f not in self.samples:
                self.samples[f] = 0
            self.samples[f] += 1

        return self.samples

    def prob_in_concept(self, obj, use_only_top=utils.MAXSIZE):
        """Return the probability that obj is in the concept,
        according to self.samples. Only the top use_only_top formulas from
        self.sample will be used; if use_only_top is not set."""

        if not self.samples:
            raise error("prob_in_concept called before formulas sampled")

        yes = 0
        total = 0
        for f, count in self.top_formulas(use_only_top):
            if self.grammar.evaluate(f, obj):
                yes += count
            total += count
        return float(yes)/total
        

    def top_formulas(self, k=5):
        """Return list of (formula, count) pairs for k most frequent
        formulas in self.samples"""

        return sorted(self.samples.items(), key=lambda (f, c): -c)[:k]

    def _regen_proposer(self):

        def proposer(formula):
            if formula is None:
                return self.grammar.random_formula()
            formula2 = formula
            while formula2 == formula:
                formula2 = self.grammar.regenerate_subtree(formula)
            return formula2

        return proposer
    
    def _regen_accept(self):

        G = self.grammar

        def accept(formula, formula2):
            log_ratio = self.log_likelihood(formula2)\
                - self.log_likelihood(formula)\
                + G.log_prior(formula2) - G.log_prior(formula)\
                + math.log(formula.size_no_leaves)\
                - math.log(formula2.size_no_leaves)\
                + G.log_prob(formula) - G.log_prob(formula2)
            return random.random() < math.exp(log_ratio)

        return accept

    @utils.memoize
    def log_likelihood(self, formula):

        W = self.world
        
        concept = set([obj for obj in W.objects
            if self.grammar.evaluate(formula, obj)])
        not_concept = W.objects - concept
        observed = W.observed_pos | W.observed_neg

        n_wrong = len(W.observed_pos & not_concept)\
            + len(W.observed_neg & concept)

        #return -utils.binomln(len(concept), len(observed & concept))\
        #    - (0 if n_wrong==0 else n_wrong*self.outlier_param)
        return -utils.binomln(len(concept), len(observed & concept))\
            - utils.binomln(len(not_concept), len(observed - concept))\
            - (0 if n_wrong==0 else n_wrong*self.outlier_param)
                # conditional necessary since self.outlier_param could
                # be inf

    def likelihood(self, formula):
        """P(world|formula)"""

        return math.exp(self.log_likelihood(formula))

