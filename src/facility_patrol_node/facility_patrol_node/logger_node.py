import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        
        self.subscription = self.create_subscription(
            Float32,
            '/intruder_distance',
            self.logger_callback,
            10)

    def logger_callback(self, msg):
        self.get_logger().info(f'[LOGGER] Intruder Distance Recorded: {msg.data:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
