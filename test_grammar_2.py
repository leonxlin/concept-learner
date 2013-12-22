

import grammar
import dnf

G = dnf.DNF(["a", "b"])

for i in xrange(10):
    f = G.random_formula()
    print f
    print G.regenerate_subtree(f)
    print 

