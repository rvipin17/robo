#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
from scipy.spatial import distance
import numpy as np
import math

rospy.init_node('Table_based_controller')
publisher = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
table_x =3
table_y =2.5
table_dia = math.sqrt(pow(table_x,2)+pow(table_y,2))

robot_x =0.0
robot_y =0.0
robot_theta=0.0


def odom_cb(msg):
	global robot_x
	global robot_y
	global robot_theta
	
	robot_x = msg.pose.pose.position.x
	robot_y = msg.pose.pose.position.y


def scancb(msg):
        x_ = []
	y_ = []
	distance_ = []
	for i in range(len(msg.ranges)):
		if msg.ranges[i]>msg.range_min and msg.ranges[i]<75.0:
			x_.append(round(msg.ranges[i]*math.cos(msg.angle_min+(i*msg.angle_increment)),3))
			y_.append(round(msg.ranges[i]*math.sin(msg.angle_min+(i*msg.angle_increment)),3))

	for i in range(len(x_)):
		distance_.append(distance.euclidean((x_[0],y_[0]),(x_[i],y_[i])))

	global robot_x
	global robot_y
	global robot_theta
	max_dist = max(distance_)
	max_index =[i for i, j in enumerate(distance_) if j == max_dist]
	vel = Twist()
	vel.linear.y= ((((y_[0]+y_[max_index[0]])/2)+robot_y)-robot_y);
	vel.linear.x= ((((x_[0]+x_[max_index[0]])/2)+robot_x)-robot_x)/10;
	publisher.publish(vel)


rospy.Subscriber("/scan",LaserScan, scancb)
rospy.Subscriber("/odom",Odometry, odom_cb)
rospy.spin()
