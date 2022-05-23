import torch.nn as nn
import torch.nn.functional as F

class Perceptron(nn.Module):
    def __init__(self):
        super(Perceptron, self).__init__()
        self.fc1 = nn.Linear(28*28, 20)
        self.fc2 = nn.Linear(20,50)
        self.fc3 = nn.Linear(50,100)
        self.fc4 = nn.Linear(100,10)
        
    def forward(self,x):
        # flatten image input
        x = x.view(-1,28*28)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x