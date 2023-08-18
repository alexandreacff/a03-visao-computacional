import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():

    package_name='miss-description'

    #Arguments
    rviz_arg = DeclareLaunchArgument(
        'rviz',
        default_value='False',
        description='Inicilize rviz or not'
    )

    gazebo_arg = DeclareLaunchArgument(
        'gazebo',
        default_value='True',
        description='Inicilize gazebo or not'
    )


    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                condition=IfCondition(LaunchConfiguration("gazebo")),
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'miss_piggy_robot'],
                        output='screen',
                        condition=IfCondition(LaunchConfiguration("gazebo"))
    )
    
      # Launch RViz2 with a configuration file
    rviz = Node(package='rviz2', executable='rviz2', 
                arguments=['-d', os.path.join(get_package_share_directory(package_name), 'configs', 'view_bot.rviz')],
                condition=IfCondition(LaunchConfiguration("rviz"))
    )
    

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["diff_cont"],
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_broad"],
    )

    # Launch them all!
    return LaunchDescription([
        #args
        rviz_arg,
        gazebo_arg,
        #nodes
        rsp,
        gazebo,
        spawn_entity,
        diff_drive_spawner,
        joint_broad_spawner,
        rviz
    ])