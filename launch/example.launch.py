import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch.actions
import launch_ros.actions

# Regarding buffered std_out behavior with launch files...
# https://github.com/ros2/launch/issues/188


def generate_launch_description():
    # Following two lines required for normal (unbuffered) std_out behavior...
    node_env = os.environ.copy()
    node_env["PYTHONUNBUFFERED"] = "1"

    parameters_file = os.path.join(
        get_package_share_directory("ros2_envirophat"), "config", "envirophat.yaml"
    )

    ld = LaunchDescription(
        [
            launch.actions.DeclareLaunchArgument(
                "envirophat_config", default_value=parameters_file
            )
        ]
    )

    ld.add_action(
        launch_ros.actions.Node(
            package="ros2_envirophat",
            node_executable="envirophat_node",
            parameters=[launch.substitutions.LaunchConfiguration("envirophat_config")],
            output="screen",
            # Following line required for normal (unbuffered) std_out behavior...
            env=node_env,
        )
    )

    return ld
