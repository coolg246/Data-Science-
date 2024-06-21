# importing libraries
import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy


# Loading the environment
environment_name = 'CartPole-v0' # mujhe cartpole ka environment chahiye
env = gym.make(environment_name) # mujhe cartpole ka environment mil gaya

# Check the environment
print(f"Observation Space: {env.observation_space}")
print(f"Action Space: {env.action_space}")
episodes = 20 # mujhe 5 episodes chahiye, episodes matlab ek game
for episode in range(1, episodes+1): # mujhe 5 episodes chahiye
    state = env.reset() # mujhe environment reset karna hai , kyun ki mujhe naya game khelna hai
    done = False # mujhe naya game khelna hai, toh mujhe done false karna hai
    score = 0 # mujhe score 0 karna hai

    while not done: # mujhe game khelna hai, toh mujhe done false karna hai
        env.render(mode='human') # mujhe game dikhana hai
        action = env.action_space.sample() # mujhe action space se koi bhi action chahiye
        n_state, reward, done, nd_done, info = env.step(action) # mujhe action ke baad mujhe naya state chahiye, mujhe reward chahiye, mujhe done chahiye, mujhe info chahiye
        score += reward # mujhe score chahiye
    print('Episode:{} Score:{}'.format(episode, score)) # mujhe episode, score
env.close() # mujhe environment close karna hai

