
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

features = ["red", "round", "hard"]
apple = Obj("apple", ["red", "round", "hard"])
orange = Obj("orange", ["round", "hard"])
blood = Obj("blood", ["red"])
water = Obj("water", [])
ball = Obj("ball", ["round", "hard"])
bird = Obj("bird", [])
pot = Obj("pot", ["hard", "round"])
bottle = Obj("bottle", ["hard", "round"])
mouse = Obj("mouse", ["round"])
redblock = Obj("redblock", ["red", "hard"])
table = Obj("table", ["hard"])
book = Obj("book", ["hard"])
grape = Obj("grape", ["round"])
chinaflag = Obj("chinaflag", ["red"])
globe = Obj("globe", ["round", "hard"])

world = World(features,
    [apple, orange, blood, ball, bird, redblock, pot,
         bottle, mouse, redblock, table, book, grape, chinaflag, globe],
    # set([apple, ball, bottle, table, globe])
    # set([apple, orange, ball, pot, bottle, redblock, table, book, globe])
    [apple, orange, grape]
    )


