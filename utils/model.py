import torch.nn as nn
import torch


class Model(nn.Module):
    def __init__(self, n=4, pre=True):
        super().__init__()

        # Encoder for images
        self.enc = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=pre)
        self.enc.fc = nn.Linear(512, 512)

        self.head = nn.Sequential(
            nn.ReLU(),
            nn.Linear(512, 150),
            nn.ReLU(),
            nn.BatchNorm1d(150),
            # nn.Dropout(0.5),
            nn.Linear(150, n)
        )

    def forward(self, x):
        x = self.enc(x)

        x = self.head(x)

        return x
