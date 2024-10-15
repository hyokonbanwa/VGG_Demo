# VGG Model Demonstration

This repository provides tools for demonstration of VGG model in real time. You will need the weights of the VGG model learned at the [following link](https://github.com/ia-gu/jikken3_vision_recognition/tree/master).

## Table of Contents

1. [Setup](#setup)
2. [Usage](#usage)

## **Warning: When using Python module “jetcam.csi_camera.CSICamera”, please be careful of the following**
(Pattern 1) You are using jetson via **ssh connection**.
- You need to remove the environment variable $DISPLAY.

bash
```bash
$ unset DISPLAY
```

python
```python
import os
os.environ.pop("DISPLAY", None)
```
(Pattern 2) You are using jetson via a **display connection**.
- You need to set the environment variable $DISPLAY to an appropriate value.

bash example
```bash
$ export DISPLAY=:0
$ xhost +
```

Reference Links
- https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_troubleshooting.html#deepstream-plugins-failing-to-load-without-display-variable-set-when-launching-ds-dockers
- https://forums.developer.nvidia.com/t/nano-nvbufsurftransform-could-not-get-egl-display-connection/81946/3

## Setup 

Note. This is only for Jetson.


1. Clone this repository.

```bash
git clone [repository URL]
cd [repository name]
```

2. Install all packages.

```bash
bash setup.sh
```

3. Test camera(**only ssh coonection**, not use diplay connection)
```bash
#check
python test_camera.py
# genrerated 256x256 image as "./image.jpg"
```
4. (only VScode) Installing VScode's jupyter extension

    
![Alt text](image.png)

5. (additonal) Correct the camera's color tone.

```bash

bash correct_color_tone.sh
```
if you restore camera`s color tone
```bash
sudo rm /var/nvidia/nvcam/settings/camera_overrides.isp
```

## Usage

1. Place the pre-trained VGG model weights in an appropriate directory.

Jupyter notebook usage


2. Set the model and model weights path for demo.ipynb.
<img width="1544" alt="image" src="https://github.com/s-ito0621/VGG_Demo/assets/131466870/7d47e6c5-07af-4923-bf5c-ec96ba9cb3af">

```bash
# default : weight_path = "final_weight.pth",model_var = "VGG11"
model_path = "[weight_path]"
model_var = "[VGG_ver]"

```

3. Run demo.ipynb

Python usage

2.  Set the model and model weights path for demo.py.

3.  Run demo.py

   ```bash
python3 demo.py
```



