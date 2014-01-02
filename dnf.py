
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
    
    def __init__(self, primitives, rules):

        rules = {x: rules[x] for x in rules} # copy
        for primitive in primitives:
            rules[primitive] = [()]
            rules[PRIMITIVE].append((primitive,))

        Grammar.__init__(self, rules, S)

#    def true_formula(self):
#        """Returns a formula that is always true, i.e., guaranteed to have
#        a nonzero posterior"""
#
#        true_conj = Formula(CONJ, (Formula(TRUE),))
#        false_disj = Formula(DISJ, (Formula(FALSE),))
#        true_disj = Formula(DISJ, (true_conj, false_disj))
#        return Formula(S, (true_disj,))

    @utils.memoize
    def evaluate(self, formula, obj):
        """Evaluate the formula at obj (boolean)"""

        # ans = formula.head.meaning(obj,
        #     [self.evaluate(f, obj) for f in formula.expansion])
        # print obj, ":", formula, "is", ans

        # return ans

        return formula.head.meaning(obj,
            [self.evaluate(f, obj) for f in formula.expansion])
        


S = PredicateSymbol("S", lambda obj, e: e[0])
DISJ = PredicateSymbol("DISJ",
    lambda obj, e: any(e),
    " | ")
CONJ = PredicateSymbol("CONJ",
    lambda obj, e: all(e),
    "&")
P = PredicateSymbol("P",
    lambda obj, e: e[0] if len(e)==1 else not e[1])
PRIMITIVE = PredicateSymbol("Primitive",
    lambda obj, e: e[0])
NEG = PredicateSymbol("!",
    lambda obj, e: False) # doesn't actually matter that this is False
TRUE = PredicateSymbol("True", lambda obj, e: True)
FALSE = PredicateSymbol("False", lambda obj, e: False)

RULE_SETS = [
    {S: [(DISJ,)],
        DISJ: [(FALSE,), (CONJ, DISJ)],
        CONJ: [(TRUE,), (P, CONJ)],
        P: [(PRIMITIVE,), (NEG, PRIMITIVE)],
        PRIMITIVE: [], # expanded in DNF.__init__
        NEG: [()],
        TRUE: [()],
        FALSE: [()]},
    {S: [(DISJ,)], # decrease the weight of TRUE and FALSE in the prior
        DISJ: [(CONJ,), (CONJ, DISJ)],
        CONJ: [(P,), (P, CONJ)],
        P: [(PRIMITIVE,), (NEG, PRIMITIVE)],
        PRIMITIVE: [(TRUE,)], # expanded in DNF.__init__
        NEG: [()],
        TRUE: [()],
        FALSE: [()]},
    {S: [(DISJ,)], # no negatives
        DISJ: [(CONJ,), (CONJ, DISJ)],
        CONJ: [(PRIMITIVE,), (PRIMITIVE, CONJ)],
        PRIMITIVE: [(TRUE,)], # expanded in DNF.__init__
        TRUE: [()]}
    ]
