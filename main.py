from BayesNetCreacion import BayesNetCreacion, Node

bnc = BayesNetCreacion()
burglar = Node("Burglar")
earthquake = Node("Earthquake")
alarm = Node("Alarm")

burglar.set_probs({0: 0.999, 1: 0.001})
earthquake.set_probs({0: 0.998, 1:0.002})
alarm.set_probs({(0, 0, 0): 0.999, (0, 0, 1): 0.001, (0, 1, 0): 0.29, (0, 1, 1): 0.71, (1, 0, 0): 0.06, (1, 0, 1): 0.94, (1, 1, 0): 0.05, (1, 1, 1): 0.95})
bnc.add_node(burglar)
bnc.add_node(earthquake)
bnc.set_cpd('Alarm|Burglar,Earthquake', alarm.get_probs)

print(bnc.cpd)




print("Hi Mom!")