from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='facility_patrol_node',
            executable='sensor',
            name='sensor_node'
        ),
        Node(
            package='facility_patrol_node',
            executable='alarm',
            name='alarm_node',
            # We can overwrite the default 20.0 threshold instantly at startup!
            parameters=[{'danger_distance': 20.0}]
        ),
        Node(
            package='facility_patrol_node',
            executable='logger',
            name='logger_node'
        ),
    ])
