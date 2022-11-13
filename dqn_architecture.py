import torch
from torch.nn import Conv2d, MaxPool2d, BatchNorm2d, Dropout2d, Sequential, Linear, AdaptiveAvgPool2d, ReLU

class ChessDQn():

    def __init__(self):
        # encoder
        super(ChessDQn, self).__init__()
        self.conv1 = Conv2d(in_channels=16, out_channels=64, kernel_size=(5, 5)) # augmente la profondeur 
        self.maxpool = MaxPool2d((2, 2)) # channels (4,4) diminue taille des canaux
        self.bn1 = BatchNorm2d(64)
        self.conv2 = Conv2d(in_channels=64, out_channels=128, kernel_size=(5, 5))
        self.bn2 = BatchNorm2d(128)
        self.conv3 = Conv2d(in_channels=128, out_channels=254)
        self.bn3 = BatchNorm2d(254)
        self.conv4 = Conv2d(in_channels=256, out_channels=512)
        self.bn4 = BatchNorm2d(512)
        self.conv5 = Conv2d(in_channels=512, out_channels=1024)
        self.bn5 = BatchNorm2d(1024) # (6,6)

        self.avgpool = AdaptiveAvgPool2d((1,1)) # -> output vecteur unittaire 1024 * (1,1)
        # MLP
        self.mlp = Sequential(
            Linear(in_features=1024, out_features=2012),
            Dropout2d(),
            ReLU(),
            Linear(in_features=2012, out_features=2012),
            ReLU(),
            Linear(in_features=2012, out_features=2500))

        # --> XOR