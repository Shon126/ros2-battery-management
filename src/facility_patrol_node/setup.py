from setuptools import setup
from glob import glob
import os

package_name = 'facility_patrol_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Tell ROS where to find our Launch files during compilation!
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='[email protected]',
    description='ROS2 Automated Facility Patrol Node',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor = facility_patrol_node.sensor_node:main',
            'alarm = facility_patrol_node.alarm_node:main',
            'logger = facility_patrol_node.logger_node:main',
        ],
    },
)
