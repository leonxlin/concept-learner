
"""Not a very good test, since it produces edited formulas that may not be
well-formed in DNF"""

import grammar
import dnf

G = dnf.DNF(["a", "b"])
f, g, h = G.random_formula(), G.random_formula(), G.random_formula()

tf, tg, th = f.random_trail(), g.random_trail(), h.random_trail()

print f, "with", f.subtree(tf), "edited is", f.replace_subtree(tf, g)
print g, "with", g.subtree(tg), "edited is", g.replace_subtree(tg, h)
print h, "with", h.subtree(th), "edited is", h.replace_subtree(th, f)
