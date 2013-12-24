
from world import BinaryFeatureObject as Obj
from world import BinaryFeatureWorld as World

table1 = {
    'A1': '0001',
    'A2': '0101',
    'A3': '0100',
    'A4': '0010',
    'A5': '1000',
    'B1': '0011',
    'B2': '1001',
    'B3': '1110',
    'B4': '1111',
    'T1': '0110',
    'T2': '0111',
    'T3': '0000',
    'T4': '1101',
    'T5': '1010',
    'T6': '1100',
    'T7': '1011'
    }

N_FEATURE = 4

def str2list(string): # gives feature list
    return [i for i in xrange(N_FEATURE) if string[i]=='1']

features = range(N_FEATURE)
name2obj= {name: Obj(name, str2list(table1[name])) for name in table1}
objects = name2obj.values()

world = World(features,
    objects,
    [obj for obj in objects if obj.name[0]=='A'],
    [obj for obj in objects if obj.name[0]=='B']
    )


