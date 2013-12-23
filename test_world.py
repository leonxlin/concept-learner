
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

features = frozenset(["red", "round", "hard"])
apple = Obj("apple", frozenset(["red", "round", "hard"]))
orange = Obj("orange", frozenset(["round", "hard"]))
blood = Obj("blood", frozenset(["red"]))
ball = Obj("ball", frozenset(["round", "hard"]))
bird = Obj("bird", frozenset([]))
redblock = Obj("redblock", frozenset(["red", "hard"]))
table = Obj("table", frozenset(["hard"]))

world = World(features,
    set([apple, orange, blood, ball, bird, redblock, table]),
    set([apple, orange, ball]))

G = world.grammar
f = G.random_formula()
print f
print {obj: G.evaluate(f, obj) for obj in world.objects}
print G.log_likelihood(f, world)
