# Deep-Learning Layers (Random)
import torch
import torch.nn as nn
class DeepNet19883(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(128, 256)
        self.act1 = nn.ReLU()
        self.fc2 = nn.Linear(256, 64)
        self.act2 = nn.Sigmoid()
    def forward(self, x):
        x = self.act1(self.fc1(x))
        x = self.act2(self.fc2(x))
        return x
print(DeepNet12248()(torch.randn(1,128)))
