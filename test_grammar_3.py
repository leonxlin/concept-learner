
import dnf

features = ["grue", "bleen"] # dumb primitives; don't allow evaluation
G = dnf.DNF(features)
f = G.random_formula()
print f
print G.prior(f)
