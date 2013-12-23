
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World
import mh

features = frozenset(["red", "round", "hard"])
apple = Obj("apple", frozenset(["red", "round", "hard"]))
orange = Obj("orange", frozenset(["round", "hard"]))
blood = Obj("blood", frozenset(["red"]))
water = Obj("water", frozenset([]))
ball = Obj("ball", frozenset(["round", "hard"]))
bird = Obj("bird", frozenset([]))
pot = Obj("pot", frozenset(["hard", "round"]))
bottle = Obj("bottle", frozenset(["hard", "round"]))
mouse = Obj("mouse", frozenset(["round"]))
redblock = Obj("redblock", frozenset(["red", "hard"]))
table = Obj("table", frozenset(["hard"]))
book = Obj("book", frozenset(["hard"]))
grape = Obj("grape", frozenset(["round"]))
chinaflag = Obj("chinaflag", frozenset(["red"]))
globe = Obj("globe", frozenset(["round", "hard"]))

world = World(features,
    set([apple, orange, blood, ball, bird, redblock, pot,
         bottle, mouse, redblock, table, book, grape, chinaflag, globe]),
    set([apple, orange, ball, pot, globe]))

G = world.grammar
f = G.random_formula()
print f
print {obj: G.evaluate(f, obj) for obj in world.objects}
print G.log_likelihood(f, world)

samples = mh.mh(mh.regen_proposer(G), mh.regen_accept(world), 100000)
profile = {}
for h in samples:
    if h not in profile:
        profile[h] = 0
    profile[h] += 1
for x in sorted(profile.items(), key=lambda (h, n): -n)[:5]:
    print x
    print G.prior(x[0])*G.likelihood(x[0], world)
