
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

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
    # set([apple, ball, bottle, table, globe])
    # set([apple, orange, ball, pot, bottle, redblock, table, book, globe])
    set([apple, orange, grape])
    )


