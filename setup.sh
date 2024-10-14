git clone https://github.com/NVIDIA-AI-IOT/jetcam
cd jetcam
pip3 install traitlets
sudo python setup.py bdist_wheel
 pip install ./dist/jetcam-0.0.0-py3-none-any.whl --user
sudo pip3 install jupyter
cd ..
