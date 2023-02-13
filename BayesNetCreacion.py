# Base
class BayesNetCreacion():
    def __init__(self):
        self.variables = ()
        self.parents = {}
        self.cpt = {}
    
    def add_node(self, node):
        query = {str(node): node.get_parents()}
        self.parents.update(query)
        self.variables += tuple(query.keys())
    
    def add_prob(self, prob):
        self.cpt.update(prob)
    
    def get_network(self):
        return {
            'variables': self.variables,
            'parents': self.parents,
            'cpt' : self.cpt
        }

    def probabilistic_inference(self, query, evidence):
        """
        Calculate the probability of the query given the evidence inputted

        :param query: the variable to calculate the prob for
        :param evidence: the evidence, given a dictionary with their values
        :return: the probability of the query happening given the evidence
        """
        result = self.enum_ask(query, evidence)
        return result[True]

    def P(self, var, e):
        """
        Calculate the probability of a variable given its parents in the network, using the conditional probability table.

        :param var: the variable to calculate the probability for
        :param e: the evidence, a dictionary that maps variables to their values
        :return: the probability of the variable given the evidence
        """  
        key = (var, e[var])
        for p in self.parents[var]:
            key += tuple(p)
            key += tuple([e[p]])
        return self.cpt[key]

    #Additional services

    def descriptiveCheck(self): #Returns if network is completely described (boolean)
        pass

    def compact(self): # Returns a compact representation of the network
        pass

    def getFactors(self): #Returns factors of the network (dict)
        return self.cpt

    def enum_ask(self, X, e): 
        QX = {}
        for xi in [True, False]:
            e[X] = xi
            QX[xi] = self.enum_all(self.variables, e)
        return self.normalize(QX)
    
    def enum_all(self, variables, e):
        if not variables:
            return 1
        Y, rest = variables[0], variables[1:]
        if Y in e:
            return self.P(Y, e) * self.enum_all(rest, e)
        else:
            return sum(self.P(Y, self.extend(e, Y ,yi))* self.enum_all(rest, self.extend(e, Y, yi))
                        for yi in [True, False])

    def extend(self, e, var, val):
        e2 = dict(e)
        e2[var] = val
        return e2

    def normalize(self, QX):
        total = sum(QX.values())
        for key in QX:
            QX[key] /= total
        return QX


#Creation of each probabilistic node that will form the network
class Node():
    def __init__(self, name):
        self.name = name
        self.parents = [] 
    
    def __str__(self):
        return self.name

    def set_parents(self, parents: list):
        self.parents = parents
    
    def get_parents(self):
        return self.parents
    
    

