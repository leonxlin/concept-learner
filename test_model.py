

import animal_world as test_world
from model import BinaryFeatureLearnerModel as Model
import mh

model = Model(test_world.world, outlier_param=7)

G = model.grammar
f = G.random_formula()

print "random formula:"
print f
print {obj: G.evaluate(f, obj) for obj in model.world.objects}
print model.log_likelihood(f)
print

print "top formulas:"
print

model.sample_formulas(3000)
for x in model.top_formulas():
    print x
    print G.prior(x[0])*model.likelihood(x[0])
    print

for obj in sorted(model.world.objects, key=lambda obj: obj.name):
    print obj, model.prob_in_concept(obj)

