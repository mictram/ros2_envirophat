#! /usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep, time

from envirophat import light, weather
import rclpy
from rclpy.node import Node
from rclpy.parameter import PARAMETER_SEPARATOR_STRING
from std_msgs.msg import Bool, String, UInt16, UInt16MultiArray


class EnvirophatNode(Node):
    def __init__(self):
        super().__init__(
            "envirophat_node",
            allow_undeclared_parameters=True,
            automatically_declare_parameters_from_overrides=True,
        )

        self.rgb_pub = self.create_publisher(UInt16MultiArray, "rgb", 10)
        self.light_pub = self.create_publisher(UInt16, "light", 10)
        self.temperature_pub = self.create_publisher(UInt16, "temperature", 10)
        self.pressure_pub = self.create_publisher(UInt16, "pressure", 10)

        self._timer = self.create_timer(
            self.get_parameter("timer_period_sec").value, self._update
        )

    def _update(self):
        try:
            self.get_logger().debug("Publishing new data ...")
            self.rgb_pub.publish(UInt16MultiArray(data=light.rgb()))
            self.light_pub.publish(UInt16(data=light.light()))
            self.temperature_pub.publish(UInt16(data=weather.temperature()))
            self.pressure_pub.publish(UInt16(data=weather.pressure()))
        except Exception as e:
            self.get_logger().error(f"Failed to publish new data. Exc: {e}")


def main(args=None):
    try:
        rclpy.init(args=args)
        node = EnvirophatNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()
    node.get_logger().info("Exiting")


if __name__ == "__main__":
    main()
