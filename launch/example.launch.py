import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="envirophat_node",
            node_executable="envirophat_node",
            output="screen"),
        ])
