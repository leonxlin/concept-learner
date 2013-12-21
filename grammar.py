
import math
import random
import utils

class Grammar:

    def __init__(self, rules, start):
        """rules is a dictionary mapping Symbols to lists of
        tuples of Symbols; start is the starting Symbol S"""

        self.rules = rules
        self.start = start

    def random_formula(self, start=None):
        """Generates a random formula by repeatedly applying
        production rules. For a given symbol, a rule is picked uniformly
        from the valid possibilities."""

        if not start:
            start = self.start
        
        expansion = tuple([self.random_formula(symbol) \
            for symbol in random.choice(self.rules[start])])
        return Formula(start, expansion)

    def prior(self, formula):
        """Gives the prior probability P(F|G) of a formula F,
        agnostic with regard to the probability probabilities: P(F|G) =
        the integral of P(F, t|G) over production probabilities t. This
        is equal to the product of beta(C_Y(F) + 1)/beta(1) over all
        non-terminal symbols Y in the derivation of F, where C_Y(F) is
        the vector of counts of the production rules used for Y and beta
        is the multinomial beta function."""

        counts = {symbol: {rewrite: 0
            for rewrite in self.rules[symbol]}
            for symbol in self.rules}
        stack = [formula]
        while stack:
            f = stack.pop()
            rewrite = tuple([f2.head for f2 in f.expansion])
            counts[f.head][rewrite] += 1
            stack.extend(f.expansion)

        priorln = 0
        for symbol in counts:
            alphas = [counts[symbol][rewrite] + 1
                for rewrite in counts[symbol]]
            one = [1]*len(alphas)
            priorln += utils.betaln(alphas) - utils.betaln(one)

        return math.exp(priorln)


class Formula:
    """An implementation that remembers the formula's derivation"""

    def __init__(self, head, expansion=()):
        """head is a Symbol; expansion is a tuple of Formulas"""

        self.head = head
        self.expansion = expansion

    def __str__(self):
        if self.expansion:
            return self.head.joiner.join(map(str, self.expansion))
        else:
            return str(self.head)

    def __repr__(self):
        return str(self)

class Symbol:
    def __init__(self, s, joiner=""):
        self.s = s
        self.joiner = joiner
    def __str__(self):
        return self.s
    def __repr__(self):
        return self.s

