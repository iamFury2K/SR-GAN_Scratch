import torch.nn as nn
from torchvision.models import vgg19
import config

class VGGLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.vgg = vgg19(pretrained=True).features[:36].eval().to(config.DEVICE)
        self.loss = nn.MSELoss()

        for params in self.vgg.parameters():
            params.requires_grad = False

    def forward(self, input, target):
        vgg_in = self.vgg(input)
        vgg_out = self.vgg(target)
        vgg_loss = self.loss(vgg_in, vgg_out)
        return vgg_loss