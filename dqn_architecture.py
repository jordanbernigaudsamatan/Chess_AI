import torch
from torch.nn import Conv2d, MaxPool2d, BatchNorm2d, Dropout2d, Sequential, Linear, AdaptiveAvgPool2d, ReLU


class ChessDQn(torch.nn.Module):

    def __init__(self):
        # encoder
        super(ChessDQn, self).__init__()
        self.conv1 = Conv2d(in_channels=14, out_channels=64, kernel_size=(3, 3)) # augmente la profondeur 
        self.maxpool = MaxPool2d((1, 1))  # channels (4,4) diminue taille des canaux
        self.bn1 = BatchNorm2d(64)
        self.conv2 = Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3))
        self.bn2 = BatchNorm2d(128)
        self.conv3 = Conv2d(in_channels=128, out_channels=254, kernel_size=(3, 3))
        self.bn3 = BatchNorm2d(254)
        """
        self.conv4 = Conv2d(in_channels=256, out_channels=512,kernel_size=(3, 3))
        self.bn4 = BatchNorm2d(512)
        self.conv5 = Conv2d(in_channels=512, out_channels=1024,kernel_size=(3, 3))
        self.bn5 = BatchNorm2d(1024)
        """
        self.avgpool = AdaptiveAvgPool2d((1, 1)) # -> output vector 254 * 1 value 
        # MLP
        self.mlp = Sequential(
            Linear(in_features=254, out_features=2012),
            Dropout2d(),
            ReLU(),
            Linear(in_features=2012, out_features=2012),
            Dropout2d(),
            ReLU(),
            Linear(in_features=2012, out_features=2564),
            Linear(in_features=2564, out_features=1))


    def forward(self, x):
        """
        take board input and output all Q-values for possible moves in chessboard
        """
        x = self.conv1(x)
        x = self.maxpool(x)
        x = self.bn1(x)

        x = self.conv2(x)
        x = self.maxpool(x)
        x = self.bn2(x)

        x = self.conv3(x)
        x = self.maxpool(x)
        x = self.bn3(x)

        x = self.avgpool(x) # [1,254,1,1]
        x = x[:,:,0,0]
        x = self.mlp(x)

        """
        x = self.conv4(x)
        x = self.maxpool(x)
        x = self.bn4()

        x = self.conv5(x)
        x = self.maxpool(x)
        x = self.bn5()
        """

        return x

"""

target_q = torch.rand((1))

dqn_policy = ChessDQn()
target_dqn = ChessDQn()
optimizer = torch.optim.Adam(dqn_policy.parameters(), lr=0.01)

dqn_policy_parameters = dqn_policy.parameters()
target_dqn._parameters = dqn_policy_parameters

dqn = ChessDQn()
test = torch.rand((14, 8, 8))
test = test[None, :]

for i in range(100):
    output = dqn(test)
    # mapping_rule step
    #max_q = torch.max(output)
    Loss = torch.nn.L1Loss()
    loss = Loss(output, target_q)
    print(output)
    print(target_q)
    print(loss.item())
    loss.backward()
    optimizer.step()
"""