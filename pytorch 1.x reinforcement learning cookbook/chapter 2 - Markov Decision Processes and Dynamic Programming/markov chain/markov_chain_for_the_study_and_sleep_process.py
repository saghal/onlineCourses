# -*- coding: utf-8 -*-
"""markov chain for the study and sleep process

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dWS6D9Y6UF0ErwhnsyEnDElF-XpEeYeZ

## import libraries
"""

import torch

"""#### transition matrix, T(s, s'), consisting of the probabilities of state s transitioning to state s'.
##### s0 (study) and s1 (sleep)
"""

T = torch.tensor([[0.4,0.6],[0.8,0.2]])

"""transition probability after k steps."""

T_2 = torch.matrix_power(T,2)
T_5 = torch.matrix_power(T,5)
T_10 = torch.matrix_power(T,10)
T_15 = torch.matrix_power(T,15)
T_20 = torch.matrix_power(T,20)

"""### define the intial distribution of two states

meaning there is a 70% chance that the process starts with study and a 30% chance that it starts with sleep.
"""

v = torch.tensor([[0.7,0.3]])

"""state distribution after k steps."""

v_1 = torch.mm(v,T)
v_2 = torch.mm(v,T_2)
v_5 = torch.mm(v,T_5)
v_10 = torch.mm(v,T_10)
v_15 = torch.mm(v,T_15)
v_20 = torch.mm(v,T_20)

print("Transition probability after 2 steps:\n{}".format(T_2))
print("Transition probability after 5 steps:\n{}".format(T_5))
print("Transition probability after 10 steps:\n{}".format(T_10))
print("Transition probability after 15 steps:\n{}".format(T_15))
print("Transition probability after 20 steps:\n{}".format(T_20))

print("Distribution of states after 1 step:\n{}".format(v_1))
print("Distribution of states after 1 step:\n{}".format(v_2))
print("Distribution of states after 1 step:\n{}".format(v_5))
print("Distribution of states after 1 step:\n{}".format(v_10))
print("Distribution of states after 1 step:\n{}".format(v_15))
print("Distribution of states after 1 step:\n{}".format(v_20))