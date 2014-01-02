
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

N_ANIMAL = 33
N_FEATURE = 102

f = open('animals', 'r')
animal_names = []
features = []
observed_pos_names = ["Ant", "Ostrich", "Tiger"]

animals = []
observed_pos = []

for i in xrange(N_ANIMAL):
    name = f.next().strip()
    animal_names.append(name)
for j in xrange(N_FEATURE):
    features.append(f.next().strip())
for i in xrange(N_ANIMAL):
    arr = f.next().split()
    assert len(arr) == N_FEATURE
    animals.append(Obj(animal_names[i],
        [features[j] for j in xrange(N_FEATURE) if arr[j] == '1']))
for name in observed_pos_names:
    observed_pos.append(animals[animal_names.index(name)])


world = World(features, animals, observed_pos)


