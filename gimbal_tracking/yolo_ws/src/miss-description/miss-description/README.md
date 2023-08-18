# miss-description

## ROS2 Control Usage

In order to execute the simulation in Gazebo with the ROS2 Controlllers you must build the workspace in the proper directory with:

 
```sh 
colcon build --symlink-install
```


and source it:

```sh
source install/setup.bash
```

Now you're able to run the launch file that executes the simulation with:

```sh
ros2 launch miss-description sim.launch.py
```

- you can add the world which the robot will be spawned adding `world:=./src/miss-description/worlds/arena_par_0.world` at the end of the launch command.


To control the robot via keyboard is possible to use:

```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```

The visualization in rviz2 its executed via the following command:

```sh
rviz2 -d ./src/miss-description/configs/view_odom_sensor.rviz
```
