# ros2_envirophat
ROS2 node for the [Pimeroni Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat)

## Suggested Hardware and Operating Systems (UNTESTED)

### Raspberry Pi 3B(+)
- [Ubuntu 18.04.3 Server for RPi3 (ARM64)](https://wiki.ubuntu.com/ARM/RaspberryPi)

### Raspberry Pi 4
- [UNOFFICIAL Ubuntu 18.04.3 Server for RPi4 (ARM64)](https://github.com/TheRemote/Ubuntu-Server-raspi4-unofficial)

### Nvidia Jetson TX2, Nano
- [Jetpack 4.2.2 (Ubuntu 18.04.3 Desktop)](https://developer.nvidia.com/embedded/jetpack#install)

## Setup

### Workspace
`mkdir -p ~/enviro_ws/src`

`cd ~/enviro_ws`

`git clone https://github.com/cheymber/ros2_envirophat.git src`

### Dependancies and Python virtual environment
`sudo apt update && sudo apt install python3-venv`

`python3 -m venv enviro && source enviro/bin/activate`

### Raspberry Pi 3B(+), 4
`pip install -r src/ros2_envirophat/requirements-pi.txt`

### Nvidia Jetson TX2, Nano
`pip install -r src/ros2_envirophat/requirements-jetson.txt`

### Build and source setup scripts
`source /opt/ros/dashing/setup.bash`

`colcon build --symlink-install`

`source install/setup.bash && source local_setup.bash`

### Launch
`ros2 launch ros2_envirohat example.launch.py`
