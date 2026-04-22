import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_path
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    # Variable for URDF File Path.
    urdf_path = os.path.join(get_package_share_path('robot_description'), 'urdf', 'robot.urdf.xacro')
    print(f"URDF File Path : {urdf_path}", end="\n\n")

    # Variable for Robot State Publisher's Parameter (robot_description). 
    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)
    print(f"Robot Description : {robot_description} ", end="\n\n")

    # Variable for RViz Configuration File Path.
    rviz_config_path = os.path.join(get_package_share_path('robot_description'), 'rviz', 'urdf_config.rviz')
    print(f"RViz Configuration File Path  : {rviz_config_path}", end="\n\n")

    # Robot State Publisher Node.
    robot_state_publisher_node = Node(
        package = "robot_state_publisher",
        executable = "robot_state_publisher",
        parameters = [{'robot_description' : robot_description}]
    )

    # Joint State Publisher Node.
    joint_state_publisher_node = Node(
        package = "joint_state_publisher_gui",
        executable = "joint_state_publisher_gui"
    )

    # RViz2 Node.
    rviz_node = Node(
        package = "rviz2",
        executable = "rviz2",
        output = "screen",
        arguments = ['-d', rviz_config_path]
    )

    # Launch Description Object.
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])