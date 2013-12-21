
import dnf

features = ["grue", "bleen"]
G = dnf.DNF(features)
f = G.random_formula()
print f
print G.prior(f)
