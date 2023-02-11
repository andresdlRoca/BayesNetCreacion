# Base
class BayesNetCreacion():
    def __init__(self):
        self.network = {}
        self.cpd = {}
    
    def add_node(self, node):
        self.cpd[str(node)] = node.probs
    
    def __str__(self) -> str:
        print(self.network)

    def set_cpd(self, relation, probs): # name|name2, name3, etc..., / {probs}
        self.cpd[relation] = probs

    def probabilistic_inference(self, target, observed):
        pass

#Creation of each probabilistic node that will form the network
class Node():
    def __init__(self, name):
        self.name = name
        self.parents = [] 
        self.probs = {}
    
    def __str__(self):
        return self.name

    def set_parents(self, parents):
        self.parents = parents
    
    def get_parents(self):
        return self.parents
    
    def set_probs(self, probs): #{0: value, 1: value} false / true
        self.probs = probs
    
    def get_probs(self):
        return self.probs
    
    

#Additional services

def descriptiveCheck(net): #Returns if network is completely described (boolean)
    pass

def compact(net): # Returns a compact representation of the network
    pass

def getFactors(net): #Returns factors of the network (dict)
    pass

def getEnum(net, query): #Returns enumeration of the network according to the query inputted
    pass