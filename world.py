
import dnf

class BinaryFeatureObject(object):
    def __init__(self, name, features):
        self.name = name
        self.features = features
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class BinaryFeatureWorld(object):

    def __init__(self, features, objects, observed_pos, observed_neg=[]):
        """features is a set of strings; objects is a list of
        BinaryFeatureObjects; concept is a set of objects"""

        self.features = set(features)
        self.objects = set(objects)
        self.observed_pos = set(observed_pos)
        self.observed_neg = set(observed_neg)




