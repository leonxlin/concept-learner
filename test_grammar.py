
import grammar

S = grammar.Symbol("S")

DISJ = grammar.Symbol("DISJ", " | ")
CONJ = grammar.Symbol("CONJ", "&")

T = grammar.Symbol("T")
P = grammar.Symbol("P")
Q = grammar.Symbol("Q")

TRUE = grammar.Symbol("True")
FALSE = grammar.Symbol("False")

rules = {S: [(DISJ,)],
    DISJ: [(FALSE,), (CONJ, DISJ)],
    CONJ: [(TRUE,), (T, CONJ)],
    T: [(P,), (Q,)],
    P: [()],
    Q: [()],
    TRUE: [()],
    FALSE: [()]}

G = grammar.Grammar(rules, S)

for i in xrange(10):
    print G.random_formula()
