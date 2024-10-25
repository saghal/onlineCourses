# -*- coding: utf-8 -*-
"""value iteration in Frozen lake

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f58TL3yHEZB25H8B16k6WHqqmZQ0m-XC

## import libraries
"""

import torch
import gym

env = gym.make("FrozenLake-v0")
gamma = 0.99
threshold = 0.0001

def run_episode(env, policy):
  state = env.reset()
  total_reward = 0
  is_done = False
  while not is_done:
    action = policy[state].item()
    state, reward, is_done, info = env.step(action)
    total_reward += reward
    if is_done:
      break
  return total_reward

def value_iteration(env, gamma, threshold):
  n_state = env.observation_space.n
  n_action = env.action_space.n
  V = torch.zeros(n_state)
  while True:
    V_temp = torch.empty(n_state)
    for state in range(n_state):
      v_actions = torch.zeros(n_action)
      for action in range(n_action):
        for trans_prob, new_state, reward, _ in env.env.P[state][action]:
          v_actions[action] += trans_prob * (reward + gamma * V[new_state])
      V_temp[state] = torch.max(v_actions)
    max_delta = torch.max(torch.abs(V - V_temp))
    V = V_temp.clone()
    if max_delta <= threshold:
      break
  return V

V_optimal = value_iteration(env, gamma, threshold)
print('Optimal values:\n{}'.format(V_optimal))

def extract_optimal_policy(env, V_optimal, gamma):

  n_state = env.observation_space.n
  n_action = env.action_space.n
  optimal_policy = torch.zeros(n_state)
  for state in range(n_state):
    v_actions = torch.zeros(n_action)
    for action in range(n_action):
      for trans_prob, new_state, reward, _ in env.env.P[state][action]:
        v_actions[action] += trans_prob * (reward+ gamma * V_optimal[new_state])
    optimal_policy[state] = torch.argmax(v_actions)
  return optimal_policy

optimal_policy = extract_optimal_policy(env, V_optimal, gamma)
print('Optimal policy:\n{}'.format(optimal_policy))

n_episode = 1000
total_rewards = []
for episode in range(n_episode):
  total_reward = run_episode(env, optimal_policy)
  total_rewards.append(total_reward)
print('Average total reward under the optimal policy: {}'.format(sum(total_rewards) / n_episode))