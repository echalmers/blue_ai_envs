import blue_ai_envs
import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make('blue_ai_envs/TransientGoals')
env.reset()
print(env.step(1))