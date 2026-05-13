import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        
        # Create Publisher for distance data
        self.publisher_ = self.create_publisher(Float32, '/intruder_distance', 10)
        
        # High-speed polling (1.0 Hz)
        self.timer = self.create_timer(1.0, self.publish_distance)

    def publish_distance(self):
        msg = Float32()
        # Simulated hardware: HC-SR04 distance
        msg.data = random.uniform(5.0, 100.0)
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'[SENSOR] Distance: {msg.data:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
