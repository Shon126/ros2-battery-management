from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Hardware Sensor Node Bring-up
        Node(
            package='battery_project',
            executable='battery_monitor',
            name='sensor_driver'
        ),
        # Alert System Node Bring-up
        Node(
            package='battery_project',
            executable='battery_alert',
            name='alert_brain'
        )
    ])

