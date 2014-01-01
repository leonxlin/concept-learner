

# Take your pick:
#import animal_world as test_world
import medin_schaffer_world as test_world
#import numbers_world as test_world

from model import BinaryFeatureLearnerModel as Model
import mh
import dnf

outlier_param = 1.3
rules = dnf.RULE_SETS[0]

print "using outlier parameter b =", outlier_param
print
print "using rules"
print rules

model = Model(test_world.world,
	 outlier_param=outlier_param,
	 rules=rules)

G = model.grammar
f = G.random_formula()

print
print "random formula:"
print f
print {obj: G.evaluate(f, obj) for obj in model.world.objects}
print model.log_likelihood(f)
print

print "top formulas:"
print

model.sample_formulas(30000)
for x in model.top_formulas():
    print x
    print G.prior(x[0])*model.likelihood(x[0])
    print

gen_probs = [(model.prob_in_concept(obj, use_only_top=10), obj)
	for obj in model.world.objects]

# objects in order of probability
for frac, obj in sorted(gen_probs, key=lambda (frac, obj): -frac):
    print "%.2f"%frac, obj

# objects in alphabetical order
print
for frac, obj in sorted(gen_probs, key=lambda (frac, obj): str(obj)):
    print "%.2f"%frac, obj
