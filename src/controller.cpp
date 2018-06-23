#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>
float goalX=-9,goalY=0; //This should come from some detection algo


geometry_msgs::Twist vel;
ros::Publisher imu_pub;
void odomCallback(const nav_msgs::OdometryConstPtr & msg)
{
	// A simple planner. It does the job for now.
	if(msg->pose.pose.position.y>=goalY)
		vel.linear.y=-1;
	else
		{
			if(msg->pose.pose.position.x>=goalX)
			{
				vel.linear.y=-0;
				vel.linear.x=-1;
			}
			else
			{
				vel.linear.x=0;
				vel.linear.y=0;
			}
		}


	imu_pub.publish(vel);
}

int main (int argc, char** argv)
{
  
	ros::init(argc,argv,"controller");
    ros::NodeHandle nh;
     imu_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
    ros::Subscriber odom_pub=nh.subscribe<nav_msgs::Odometry>("/odom",1000,odomCallback);

    ros::Rate loop_rate(100);
    sleep(5);
    while(ros::ok())
    {
        ros::spinOnce();
        loop_rate.sleep();
    }
}
