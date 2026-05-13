import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

import logging
from datetime import datetime


class AlertNode(Node):

    def __init__(self):

        super().__init__('alert_brain')

        # Declare live parameter
        self.declare_parameter('warning_threshold', 20)

        # Create subscriber
        self.subscription = self.create_subscription(
            Int32,
            '/battery_level',
            self.battery_callback,
            10
        )

        # Configure log file
        logging.basicConfig(
            filename='battery_alert.log',
            level=logging.WARNING,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        self.get_logger().info('Alert Brain Started')


    def battery_callback(self, msg):

        # Read live parameter
        threshold = self.get_parameter(
            'warning_threshold'
        ).value

        if msg.data <= threshold:

            warning_msg = (
                f'CRITICAL WARNING! Battery at {msg.data}%'
            )

            # Terminal log
            self.get_logger().error(warning_msg)

            # File log
            logging.warning(warning_msg)

        else:

            self.get_logger().info(
                f'Battery OK: {msg.data}%'
            )


def main(args=None):

    rclpy.init(args=args)

    node = AlertNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
