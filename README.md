# robo
1) The first stage begins with an omni-directional robot parked in front of a table. The four legs of the table are visible to the Lidar sensor at the centre of the robot.
2) In the second stage, the robot will then find its way to go underneath the table, and it will align and center itself within 4 legs of the table as shown in the picture attached. Additionally the robot will response to the movement of the table accordingly.

### Prerequisites

1) Install ROS Kinetic with ubuntu 16.04.
2) Install Python, pip, and Scipy.

### Instructions

1) create a workspace
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
$ cd ..
$ catkin_make
   
2) Clone the project to catkin_ws/src
$ cd ~/catkin_ws/src
$ git clone https://github.com/rvipin17/robo.git
$ cd ..
$ catkin_make
