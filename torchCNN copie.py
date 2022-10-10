from torch import nn
from torch.opti import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transform import ToTensor
 
train=datasets.MNIST(root='data', )