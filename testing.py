from BayesNetCreacion import BayesNetCreacion, Node

bnc = BayesNetCreacion()
burglary = Node("Burglary")
earthquake = Node("Earthquake")
alarm = Node("Alarm")
johncalls = Node("JohnCalls")
marycalls = Node("MaryCalls")


burglary.set_probs({0: 0.999, 1: 0.001})
earthquake.set_probs({0: 0.998, 1:0.002})
alarm.set_parents([str(burglary), str(earthquake)])
alarm.set_cpds({(0, 0, 0): 0.999, (0, 0, 1): 0.001, (0, 1, 0): 0.29, (0, 1, 1): 0.71, (1, 0, 0): 0.06, (1, 0, 1): 0.94, (1, 1, 0): 0.05, (1, 1, 1): 0.95})
johncalls.set_parents(str(alarm))
marycalls.set_parents(str(alarm))
johncalls.set_cpds({(1,0): 0.05, (1,1):0.90, (0,1):0.70, (0,0):0.01})

bnc.add_node(burglary)
bnc.add_node(earthquake)
bnc.add_node(alarm)
bnc.add_node(johncalls)
bnc.add_node(marycalls)

print(bnc.get_network())

