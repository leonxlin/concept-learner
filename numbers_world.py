
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

observed_nums = [60, 80, 10, 30, 23, 25, 21]

nums = range(1, 101)
DIVISOR_SET = range(2, 31)
NEAR_SET = range(3, 101, 3)
#DIVISOR_SET = xrange(2, 21)
#NEAR_SET = [5*i for i in xrange(1, 20)]

features = ["near" + str(i) for i in NEAR_SET]\
    + ["mult" + str(i) for i in DIVISOR_SET]

objs = [Obj(str(i), ["near" + str(j) for j in NEAR_SET if abs(j-i)<6]
    + ["mult" + str(j) for j in DIVISOR_SET if i%j==0]) 
	for i in nums]

observed = [objs[i-1] for i in observed_nums]

world = World(features, objs, observed)
