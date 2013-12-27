
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

nums = range(1, 101)
features = ["near" + str(i) for i in nums]\
    + ["mult" + str(i) for i in nums]

objs = [Obj(str(i), ["near" + str(j) for j in nums if abs(j-i)<6]
    + ["mult" + str(j) for j in nums if i%j==0]) for i in nums]

world = World(features, objs, [40, 50])
