# Base
class BayesNetCreacion():
    def __init__(self):
        self.network = {}
    
    def add_node(self, node):
        self.network[str(node)] = node.get_info()
    
    def get_network(self):
        return self.network

    def probabilistic_inference(self, observed, target):
        evidence = self.getEnum(observed, {})
        prob_target = self.getEnum(target, observed)
        result = prob_target/evidence
        return result

    #Additional services

    def descriptiveCheck(self): #Returns if network is completely described (boolean)
        pass

    def compact(self): # Returns a compact representation of the network
        pass

    def getFactors(self): #Returns factors of the network (dict)
        pass

    def getEnum(self, observed, target): #Returns enumeration of the network according to the query inputted
        enumThis = {**observed, **target}
        variable = observed.pop()
        

#Creation of each probabilistic node that will form the network
class Node():
    def __init__(self, name):
        self.name = name
        self.parents = [] 
        self.probs = {}
        self.cpds = {}
    
    def __str__(self):
        return self.name

    def set_parents(self, parents):
        self.parents = parents
    
    def get_parents(self):
        return self.parents
    
    def set_probs(self, probs): #{False: value, True: value} 
        self.probs = probs
    
    def get_probs(self):
        return self.probs

    def set_cpds(self, cpds):
        self.cpds = cpds
    
    def get_cpds(self):
        return self.cpds
    
    def get_info(self):
        return {
            'parents': self.get_parents(),
            'values': self.get_probs(),
            'cpds': self.get_cpds()
        }
    
    

