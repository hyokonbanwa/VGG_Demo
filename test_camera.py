import os
import gc
import cv2
from jetcam.csi_camera import CSICamera

gc.collect()
os.environ.pop("DISPLAY", None)
camera = CSICamera(width=256, height=256, capture_device=0)
print("camera enabled")
image = camera.read()
image_path = "image.jpg"
cv2.imwrite(image_path, image)
