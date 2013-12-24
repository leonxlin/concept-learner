

import test_world
from model import BinaryFeatureLearnerModel as Model
import mh

model = Model(test_world.world)

G = model.grammar
f = G.random_formula()

print "random formula:"
print f
print {obj: G.evaluate(f, obj) for obj in model.world.objects}
print model.log_likelihood(f)
print

print "top formulas:"
print

samples = model.sample_formulas()
profile = {}
for h in samples:
    if h not in profile:
        profile[h] = 0
    profile[h] += 1
for x in sorted(profile.items(), key=lambda (h, n): -n)[:5]:
    print x
    print G.prior(x[0])*model.likelihood(x[0])
    print
