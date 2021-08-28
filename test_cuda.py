import torch

tensor = torch.randn((256, 256))
tensor = tensor**2
print("test cuda successfully")