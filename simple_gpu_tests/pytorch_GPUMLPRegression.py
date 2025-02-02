#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

# torch.manual_seed(1)    # reproducible

x = torch.unsqueeze(
    torch.linspace(-1, 1, 100), dim=1
)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2 * torch.rand(x.size())  # noisy y data (tensor), shape=(100, 1)

if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # hidden layer
        self.predict = torch.nn.Linear(n_hidden, n_output)  # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))  # activation function for hidden layer
        x = self.predict(x)  # linear output
        return x


net = Net(n_feature=1, n_hidden=30, n_output=1)  # define the network
if torch.cuda.is_available():
    net = net.cuda()

print(net)  # net architecture

optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss

plt.ion()  # something about plotting

for t in range(500):
    prediction = net(x)  # input x and predict based on x
    loss = loss_func(prediction, y)  # must be (1. nn output, 2. target)

    optimizer.zero_grad()  # clear gradients for next train
    loss.backward()  # backpropagation, compute gradients
    optimizer.step()  # apply gradients

    print("loss at step" + str(t) + " is:" + str(loss.data))

    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        if x.is_cuda:
            plt.scatter(x.cpu().data.numpy(), y.cpu().data.numpy())
            plt.plot(x.cpu().data.numpy(), prediction.cpu().data.numpy(), "r-", lw=5)
            plt.text(
                0.5,
                0,
                "Loss=%.4f" % loss.cpu().data.numpy(),
                fontdict={"size": 20, "color": "red"},
            )
            plt.pause(0.1)
        else:
            plt.scatter(x.data.numpy(), y.data.numpy())
            plt.plot(x.data.numpy(), prediction.data.numpy(), "r-", lw=5)
            plt.text(
                0.5,
                0,
                "Loss=%.4f" % loss.data.numpy(),
                fontdict={"size": 20, "color": "red"},
            )
            plt.pause(0.1)

plt.ioff()
plt.show()
