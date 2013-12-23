
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

    def __init__(self, features, objects, concept):
        """features is a set of strings; objects is a list of
        BinaryFeatureObjects; concept is a set of objects"""

        self.features = features
        self.objects = objects 
        self.concept = concept

        def feature_decider(feat):
            return lambda obj, e: feat in obj.features

        symbols = [dnf.PredicateSymbol(str(feat),
            feature_decider(feat)) for feat in features]
        self.grammar = dnf.DNF(symbols)
