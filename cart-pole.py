import gym
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

MAX_STEPS = 200
MAX_EPISODES = 1000

# get the cartpole environment and set up the scaffolding for an MDP problem

# class LinearAgent(nn.Module):
#     def __init__(self, input_size, output_size, env):
#         super(LinearAgent, self).__init__()
#         self.linear = torch.nn.Linear(input_size, output_size)
#         self.env = env

#     def forward(self, x):
#         output = self.linear(x)
#         return output

#     def evaluate(self):
#         state = self.env.reset()
#         for t in range(max_t):
#             state = torch.from_numpy
        
        
        


def main():

    # learning by doing, kvfran solution approach
    # initialize the parameters using numpy, there is one per observation, so total of 4, the multiply and subtract is a trick to take a range from 0..1 to -1..1

    # ok 

    env = gym.make('CartPole-v0')
    print(f"observation space: {env.observation_space} action space: {env.action_space}")
    best_params =  None
    best_reward = 0
   
    def run_episode(parameters):
        observation = env.reset()
        total_reward = 0
        for _ in range(MAX_STEPS):
            env.render()
            # so now you do the inner product (weighted sum) of the parameter vector and the observation vector, and since the action is binary you can use the sign
            # to decide on the action to take
            action = 0 if np.matmul(parameters, observation) < 0 else 1
            observation, reward, done, _ = env.step(action) # take an action
            total_reward += reward
            if done:
                break
        env.close()
        return total_reward
            # important to recognize that it doesn't matter which direction you make the sign here, because the algorithm will adjust the weights 
            # in the proper direction to maximize reward if you set it up right

    for episode in range(MAX_EPISODES):
        parameters = np.random.rand(4) * 2 - 1
        reward = run_episode(parameters)
        if reward > best_reward:
            best_reward = reward
            best_params = parameters
            if reward == 200:
                print(f"solved environment in {episode} episodes")
                break
    



if __name__=='__main__':
    main()