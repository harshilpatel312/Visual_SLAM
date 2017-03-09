#include <ros/ros.h>
// PCL specific includes
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>


void cloud_cb (const sensor_msgs::PointCloud2ConstPtr& input)
{
ROS_INFO_STREAM(*input);

}

int main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv,"my_pcl_tutorial");
  ros::NodeHandle nh;

  // Create a ROS subscriber for the input point cloud
  ros::Subscriber sub = nh.subscribe ("/camera/depth/points", 1, cloud_cb);

  // Spin
  ros::spin ();
}

