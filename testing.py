from BayesNetCreacion import BayesNetCreacion, Node

bnc = BayesNetCreacion()
burglar = Node("Burglar")
earthquake = Node("Earthquake")
alarm = Node("Alarm")

burglar.set_probs({0: 0.999, 1: 0.001})
earthquake.set_probs({0: 0.998, 1:0.002})
alarm.set_parents([str(burglar), str(earthquake)])
alarm.set_probs({(0, 0, 0): 0.999, (0, 0, 1): 0.001, (0, 1, 0): 0.29, (0, 1, 1): 0.71, (1, 0, 0): 0.06, (1, 0, 1): 0.94, (1, 1, 0): 0.05, (1, 1, 1): 0.95})
bnc.add_node(burglar)
bnc.add_node(earthquake)
bnc.set_cpd('Alarm|Burglar,Earthquake', alarm)

# # p = bnc.probabilistic_inference({})

# def joint_probability(B, E, A):
#     joint_probability = burglar.get_probs()[B] * earthquake.get_probs()[E] * alarm.get_probs()[A]
#     return joint_probability

# joint = joint_probability(1, 1, (1,1,0))

# def probabilistic_inference(joint_prob, observed_values):
#     normalization_constant = sum(joint_prob[b_e_a] for b_e_a in joint_prob if all(val == observed_values[i] for i, val in enumerate(b_e_a)))


print("Hi Mom!")