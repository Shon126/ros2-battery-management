import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SensorNode(Node):

    def __init__(self):
        super().__init__('sensor_node')

        self.publisher_ = self.create_publisher(
            String,
            '/warning_alert',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_warning
        )

    def publish_warning(self):

        msg = String()
        msg.data = "WARNING: Obstacle detected!"

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing: {msg.data}'
        )

def main(args=None):

    rclpy.init(args=args)

    node = SensorNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
