# -*- coding: utf-8 -*-
"""coin-flipping gamble problem with value iteration

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NaRDR_b9HM8g3Wtl_y6nHxvAYfjjex0p

## import libraries
"""

import torch

gamma = 1
threshold = 1e-10

"""define env"""

capital_max = 100
n_state = capital_max + 1
rewards = torch.zeros(n_state)
rewards[-1] = 1

"""probability of getting heads is 40%"""

head_prob = 0.4

env = {'capital_max': capital_max,
       'head_prob': head_prob,
       'rewards': rewards,
       'n_state': n_state}

def value_iteration(env, gamma, threshold):
  head_prob = env['head_prob']
  n_state = env['n_state']
  capital_max = env['capital_max']
  V = torch.zeros(n_state)

  while True: 
    V_temp = torch.zeros(n_state)
    for state in range(1, capital_max):    
      v_actions = torch.zeros(min(state, capital_max - state) + 1)
      for action in range(1, min(state, capital_max - state) + 1):
        v_actions[action] += head_prob * (rewards[state + action] + gamma * V[state + action])
        v_actions[action] += (1 - head_prob) * (rewards[state - action] + gamma * V[state - action])
      V_temp[state] = torch.max(v_actions)
    max_delta = torch.max(torch.abs(V - V_temp))
    V = V_temp.clone()
    if max_delta <= threshold:  
      break
    
  return V

def extract_optimal_policy(env, V_optimal, gamma):
  head_prob = env['head_prob']
  n_state = env['n_state']
  capital_max = env['capital_max']
  optimal_policy = torch.zeros(capital_max).int()
  for state in range(1, capital_max):
    v_actions = torch.zeros(n_state)
    for action in range(1,min(state, capital_max - state) + 1):
      v_actions[action] += head_prob * ( rewards[state + action] + gamma * V_optimal[state + action])
      v_actions[action] += (1 - head_prob) * (rewards[state - action] + gamma * V_optimal[state - action])
    optimal_policy[state] = torch.argmax(v_actions)
  return optimal_policy

V_optimal = value_iteration(env, gamma, threshold)
optimal_policy = extract_optimal_policy(env, V_optimal, gamma)
print('Optimal values:\n{}'.format(V_optimal))
print('Optimal policy:\n{}'.format(optimal_policy))

import matplotlib.pyplot as plt
plt.plot(optimal_policy[:100].numpy())
plt.title('Optimal policy')
plt.xlabel('state')
plt.ylabel('action')
plt.show()