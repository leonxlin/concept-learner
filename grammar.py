
import random

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

