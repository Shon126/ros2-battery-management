import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BatteryNode(Node):
    def __init__(self):
        super().__init__('battery_node')
        
        # Instantiate Publisher
        self.publisher_ = self.create_publisher(Int32, '/battery_level', 10)
        
        # Initial Hardware State
        self.battery_percentage = 100
        
        # High-Frequency Polling Loop (1.0 Hz)
        self.timer = self.create_timer(5.0, self.drain_battery)

    def drain_battery(self):
        if self.battery_percentage > 0:
            self.battery_percentage -= 5
            
        msg = Int32()
        msg.data = self.battery_percentage
        
        self.publisher_.publish(msg)
        self.get_logger().info(f"[HARDWARE SENSOR] Battery Level: {msg.data}%")

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
