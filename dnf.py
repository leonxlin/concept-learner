
# module for disjunctive normal form

from grammar import *
import utils
import math



class PredicateSymbol(Symbol):
    def __init__(self, name, meaning, joiner=""):
        """meaning(object, expansion_meanings) is a boolean function"""
        Symbol.__init__(self, name, joiner)
        self.meaning = meaning

class DNF(Grammar):
    
    def __init__(self, primitives):

        rules = DNF_COMMON_RULES
        for primitive in primitives:
            rules[primitive] = [()]
            rules[PRIMITIVE].append((primitive,))

        Grammar.__init__(self, rules, S)

    @utils.memoize
    def evaluate(self, formula, obj):
        """Evaluate the formula at obj (boolean)"""

        # ans = formula.head.meaning(obj,
        #     [self.evaluate(f, obj) for f in formula.expansion])
        # print obj, ":", formula, "is", ans

        # return ans

        return formula.head.meaning(obj,
            [self.evaluate(f, obj) for f in formula.expansion])

    @utils.memoize
    def log_likelihood(self, formula, world):
        
        count = 0
        
        for obj in world.objects:
            if self.evaluate(formula, obj):
                count += 1
            elif obj in world.concept:
                return -float('Inf')

        return -utils.binomln(count, len(world.concept))

    def likelihood(self, formula, world):
        """P(world|formula)"""

        return math.exp(self.log_likelihood(formula, world))
        


S = PredicateSymbol("S", lambda obj, e: e[0])
DISJ = PredicateSymbol("DISJ",
    lambda obj, e: e[0] if len(e)==1 else e[0] or e[1],
    " | ")
CONJ = PredicateSymbol("CONJ",
    lambda obj, e: e[0] if len(e)==1 else e[0] and e[1],
    "&")
P = PredicateSymbol("P",
    lambda obj, e: e[0] if len(e)==1 else not e[1])
PRIMITIVE = PredicateSymbol("Primitive",
    lambda obj, e: e[0])
NEG = PredicateSymbol("!",
    lambda obj, e: False) # doesn't actually matter that this is False
TRUE = PredicateSymbol("True", lambda obj, e: True)
FALSE = PredicateSymbol("False", lambda obj, e: False)

DNF_COMMON_RULES = {S: [(DISJ,)],
    DISJ: [(FALSE,), (CONJ, DISJ)],
    CONJ: [(TRUE,), (P, CONJ)],
    P: [(PRIMITIVE,), (NEG, PRIMITIVE)],
    PRIMITIVE: [],
    NEG: [()],
    TRUE: [()],
    FALSE: [()]}
