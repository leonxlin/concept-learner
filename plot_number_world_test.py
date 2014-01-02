
import numbers_world as test_world

from model import BinaryFeatureLearnerModel as Model
import dnf

outlier_param = 1.3
rules = dnf.RULE_SETS[1]

print "using outlier parameter b =", outlier_param
print
print "using rules"
print rules

model = Model(test_world.world,
	 outlier_param=outlier_param,
	 rules=rules)

G = model.grammar

print "top formulas:"
print

model.sample_formulas(25000)
for x in model.top_formulas():
    print x
    print G.prior(x[0])*model.likelihood(x[0])
    print

gen_probs = sorted([(model.prob_in_concept(obj, use_only_top=10), obj)
	for obj in model.world.objects], key=lambda (f, ob): int(str(ob)))
#gen_probs = sorted([(model.prob_in_concept(obj), obj)
	#for obj in model.world.objects], key=lambda (f, ob): int(str(ob)))

print
for frac, obj in gen_probs:
    print "%.2f"%frac, obj


import matplotlib.pyplot as plt
plt.vlines(test_world.nums, 0, [f for f, obj in gen_probs], linewidths=2)
plt.show()


