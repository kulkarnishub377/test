# CNN Model
import torch.nn as nn
class MiniCNN29056(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 16, 3, padding=1)
        self.fc = nn.Linear(16*32*32, 10)
