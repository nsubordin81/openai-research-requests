import gym

import torch
import torch.nn as nn
import torch.nn.functional as F

# get the cartpole environment and set up the scaffolding for an MDP problem

class LinearAgent(nn.Module):
    def __init__(self, input_size, output_size, env):
        super(LinearAgent, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)
        self.env = env

    def forward(self, x):
        output = self.linear(x)
        return output

    def evaluate(self):
        state = self.env.reset()
        for t in range(max_t):
            state = torch.from_numpy
        
        
        


def main():

    env = gym.make('CartPole-v0')
    print(f"observation space: {env.observation_space} action space: {env.action_space}")
    env.reset()

    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample()) # take an action
    env.close()


if __name__=='__main__':
    main()