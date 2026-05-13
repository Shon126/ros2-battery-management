import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class AlarmNode(Node):
    def __init__(self):
        super().__init__('alarm_node')
        
        # Live configurable threshold (Default: 20.0 cm)
        self.declare_parameter('danger_distance', 20.0)
        
        # Subscribe to the sensor data
        self.subscription = self.create_subscription(
            Float32,
            '/intruder_distance',
            self.alarm_callback,
            10)

    def alarm_callback(self, msg):
        distance = msg.data
        
        # Fetch the LIVE parameter value every time a message arrives
        current_threshold = self.get_parameter('danger_distance').value
        
        # Evaluate Intrusion
        if distance < current_threshold:
            self.get_logger().error(f'[ALARM] INTRUDER DETECTED! Distance = {distance:.2f} cm')
        else:
            self.get_logger().info('[SECURITY] Area Safe')

def main(args=None):
    rclpy.init(args=args)
    node = AlarmNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
