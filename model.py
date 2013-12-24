
import world
import dnf
import mh
import utils
import math
import random

class BinaryFeatureLearnerModel(object):

    def __init__(self, world):
        self.world = world

        # define grammar

        def feature_decider(feat):
            return lambda obj, e: feat in obj.features
        symbols = [dnf.PredicateSymbol(str(feat),
            feature_decider(feat)) for feat in world.features]
        self.grammar = dnf.DNF(symbols)

    def sample_formulas(self, n=30000):
        
        return mh.mh(self._regen_proposer(), self._regen_accept(), n)

    def _regen_proposer(self):

        def proposer(formula):
            if formula is None:
                return self.grammar.true_formula()
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
        
        count = 0
        
        for obj in self.world.objects:
            if self.grammar.evaluate(formula, obj):
                count += 1
            elif obj in self.world.concept:
                return -float('Inf')

        return -utils.binomln(count, len(self.world.concept))

    def likelihood(self, formula):
        """P(world|formula)"""

        return math.exp(self.log_likelihood(formula))

