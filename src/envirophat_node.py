from time import sleep, time

# from ros2_utils.callbacks import log_level as llcb

from envirophat import light
import rclpy
from std_msgs.msg import Bool, String, UInt16, UInt16MultiArray


class EnvirophatNode:

    def __init__(self):
        self.rate = 10
        self.node = rclpy.create_node('envirophat_node')
        self.logger = self.node.get_logger()

        self.rgb_pub = self.node.create_publisher(UInt16MultiArray, 'rgb')

        # self.log_level_sub = self.node.create_subscription(String, 'log_level', lambda msg: llcb(msg, self.node), 10)

    def run(self):
        self.logger.info(f'Starting loop rate at {self.rate} hz...')
        while True:
            start = time()
            rclpy.spin_once(self.node, timeout_sec=0.01)

            self.bat_pub.publish(UInt16MultiArray(data=light.rgb()))

            remain = 1 / self.rate + start - time()
            if remain > 0:
                sleep(remain)


def main():
    try:
        rclpy.init()
        node = EnvirophatNode()
        node.run()
    except KeyboardInterrupt:
        rclpy.shutdown()
        pass
    node.logger.info('Exiting')


if __name__ == '__main__':
    main()
