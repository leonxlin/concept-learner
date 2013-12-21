
# module for disjunctive normal form

from grammar import *


S = Symbol("S")
DISJ = Symbol("DISJ", " | ")
CONJ = Symbol("CONJ", "&")
P = Symbol("P")
FEATURE = Symbol("Feature")
NEG = Symbol("!")
TRUE = Symbol("True")
FALSE = Symbol("False")

DNF_COMMON_RULES = {S: [(DISJ,), (TRUE,), (FALSE,)],
    DISJ: [(P,), (CONJ, DISJ)],
    CONJ: [(P,), (P, CONJ)],
    P: [(FEATURE,), (NEG, FEATURE)],
    FEATURE: [],
    NEG: [()],
    TRUE: [()],
    FALSE: [()]}


class DNF(Grammar):
    
    def __init__(self, features):

        rules = DNF_COMMON_RULES
        for feature in features:
            s = Symbol(str(feature))
            rules[s] = [()]
            rules[FEATURE].append((s,))

        Grammar.__init__(self, rules, S)
