import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlarmNode(Node):

    def __init__(self):

        super().__init__('alarm_node')

        self.subscription = self.create_subscription(
            String,
            '/warning_alert',
            self.alarm_callback,
            10
        )

    def alarm_callback(self, msg):

        self.get_logger().info(
            f'ALARM: {msg.data}'
        )

def main(args=None):

    rclpy.init(args=args)

    node = AlarmNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
