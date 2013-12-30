

# Take your pick:
#import animal_world as test_world
#import medin_schaffer_world as test_world
import numbers_world as test_world

from model import BinaryFeatureLearnerModel as Model
import mh
import dnf

# model = Model(test_world.world, outlier_param=2)
model = Model(test_world.world, rules=dnf.RULE_SETS[1])

G = model.grammar
f = G.random_formula()

print "random formula:"
print f
print {obj: G.evaluate(f, obj) for obj in model.world.objects}
print model.log_likelihood(f)
print

print "top formulas:"
print

model.sample_formulas(1000)
for x in model.top_formulas():
    print x
    print G.prior(x[0])*model.likelihood(x[0])
    print

for frac, obj in sorted([(model.prob_in_concept(obj, use_only_top=10), obj)
        for obj in model.world.objects], key=lambda (frac, obj): -frac):
    print "%3f"%frac, obj

