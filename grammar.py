
import math
import random
import utils
import numpy
from bisect import bisect_left

class Grammar:

    def __init__(self, rules, start):
        """rules is a dictionary mapping Symbols to lists of
        tuples of Symbols; start is the starting Symbol S"""

        self.rules = rules
        self.start = start

        self._symbol_list = list(rules.keys())
        self._ln_rule_counts = numpy.log([len(rules[s])
            for s in self._symbol_list])

    @utils.memoize
    def prob(self, formula):
        """Gives the probability P(F|G, sigma) that
        random_formula returns F=formula. Note that random_formula
        assumes a uniform distribution sigma over the production rules
        for a given nonterminal symbol."""
        
        profile = self.rule_profile(formula)
        symbol_counts = [sum(profile[symbol].values())
            for symbol in self._symbol_list]
        probln = -numpy.dot(self._ln_rule_counts, symbol_counts)
        return math.exp(probln)

    @utils.memoize
    def _prob(self, formula):
        """An alternate implementation of prob."""

        return numpy.prod([1./len(self.rules[formula.head])]
            + [self._prob(f) for f in formula.expansion])
        
    def regenerate_subtree(self, formula):
        """Returns a new Formula with a random subtree of formula
        regenerated"""

    def random_formula(self, start=None):
        """Generates a random formula by repeatedly applying
        production rules. For a given symbol, a rule is picked uniformly
        from the valid possibilities."""

        if not start:
            start = self.start
        
        expansion = tuple([self.random_formula(symbol) \
            for symbol in random.choice(self.rules[start])])
        return Formula(start, expansion)

    @utils.memoize
    def rule_profile(self, formula):
        """Returns a dictionary from symbols to dictionaries from
        symbol-tuples to the number of times the associated production
        rule occurs in formula's derivation""" 

        counts = {symbol: {rewrite: 0
            for rewrite in self.rules[symbol]}
            for symbol in self.rules}
        stack = [formula]
        while stack:
            f = stack.pop()
            rewrite = tuple([f2.head for f2 in f.expansion])
            counts[f.head][rewrite] += 1
            stack.extend(f.expansion)

        return counts

    @utils.memoize
    def prior(self, formula):
        """Gives the prior probability P(F|G) of a formula F,
        agnostic with regard to the production probabilities: P(F|G) =
        the integral of P(F, t|G) over production probabilities t. This
        is equal to the product of beta(C_Y(F) + 1)/beta(1) over all
        non-terminal symbols Y in the derivation of F, where C_Y(F) is
        the vector of counts of the production rules used for Y and beta
        is the multinomial beta function."""

        counts = self.rule_profile(formula)

        priorln = 0
        for symbol in counts:
            alphas = [counts[symbol][rewrite] + 1
                for rewrite in counts[symbol]]
            one = [1]*len(alphas)
            priorln += utils.betaln(alphas) - utils.betaln(one)

        return math.exp(priorln)


@utils.memoize
class Formula:
    """Stores the parse-tree of a formula"""

    def __init__(self, head, expansion=()):
        """head is a Symbol; expansion is a tuple of Formulas"""

        self.head = head
        self.expansion = expansion

        self.size = 1 + sum([f.size for f in expansion])
        self.size_no_leaves = (1 if expansion else 0)\
            + sum([f.size_no_leaves for f in expansion])

    def random_trail(self):
        """Returns a list of indices of expansions, which when
        followed starting from self points to a subtree of the formula"""

        r = random.randint(1, self.size_no_leaves)
        index = bisect_left(self._cum_sizes_no_leaves(), r) - 1
        if index == -1:
            return []
        else:
            return [index] + self.expansion[index].random_trail()

    def subtree(self, trail):
        """Returns the subtree (a Formula) corresponding to a
        trail of expansion indices"""

        if not trail:
            return self
        return self.expansion[trail[0]].subtree(trail[1:])

    def replace_subtree(self, trail, formula):
        """Returns a new Formula identical to self except for the
        subtree at trail, which is replaced with formula"""

        if not trail:
            return formula

        expansion = tuple([f.replace_subtree(trail[1:], formula)\
            if trail[0]==i else f\
            for i, f in enumerate(self.expansion)])

        return Formula(self.head, expansion)

    @utils.memoize
    def _cum_sizes_no_leaves(self):
        cum = [1]
        for f in self.expansion:
            cum.append(cum[-1] + f.size_no_leaves)
        return cum

    def __str__(self):
        if self.expansion:
            return self.head.joiner.join(map(str, self.expansion))
        else:
            return str(self.head)

    def __repr__(self):
        return str(self)


@utils.memoize
class Symbol:
    def __init__(self, s, joiner=""):
        self.s = s
        self.joiner = joiner
    def __str__(self):
        return self.s
    def __repr__(self):
        return self.s

