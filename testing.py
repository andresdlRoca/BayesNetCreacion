from BayesNetCreacion import BayesNetCreacion, Node

bnc = BayesNetCreacion()
burglar = Node("Burglar")
earthquake = Node("Earthquake")
alarm = Node("Alarm")

burglar.set_probs({0: 0.999, 1: 0.001})
earthquake.set_probs({0: 0.998, 1:0.002})
alarm.set_parents([str(burglar), str(earthquake)])
alarm.set_cpds({(False, False, False): 0.999, (False, False, True): 0.001, (False, True, False): 0.29, (False, True, True): 0.71, (True, False, False): 0.06, (True, False, True): 0.94, (True, True, False): 0.05, (True, True, True): 0.95})

bnc.add_node(burglar)
bnc.add_node(earthquake)
bnc.add_node(alarm)

print(bnc.get_network())

print("Hi Mom!")