
import traitlets
from jetcam.utils import bgr8_to_jpeg
from IPython.display import display
import ipywidgets
from jetcam.csi_camera import CSICamera
import cv2
import torch
from torch import nn, optim
import numpy as np
import random
import sys
from src.vgg_local import VGG_LOCAL
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image
import gc

model_path = "./final_weight.pth"
model_ver = "VGG11"
RPS_list = ["チョキ", "グー", "パー"]

camera = CSICamera(width=64, height=64, capture_device=0)  


input("撮影します. Enterキーを押してください")

# gc.collect()
image = camera.read()

image_path = "./image.jpg"
cv2.imwrite(image_path, image) 

print("撮影が終わりました")

image_size = 64
# Set random seed for reproducibility
random_seed = 9999
random.seed(random_seed)
np.random.seed(random_seed)
torch.manual_seed(random_seed)
if torch.cuda.is_available():
    device = torch.device('cuda')
    torch.cuda.manual_seed(random_seed)
    torch.backends.cudnn.deterministic = True
else:
    device = torch.device('cpu')
# Preprocessing for test data
test_transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])


input = test_transform(Image.fromarray(image))
# Initialize and load model weights
model = VGG_LOCAL(model_ver, classes=3, image_size=image_size).to(device)
model.load_state_dict(torch.load(model_path))
print("モデルの読み込み完了．推論開始")
model.eval()
with torch.no_grad():
    input = input.to(device)
    output = model(input.unsqueeze(0))

print(f'{RPS_list[torch.argmax(output)]}です')
