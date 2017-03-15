#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from matplotlib import pyplot as plt

pub = rospy.Publisher('cv_image', Image, queue_size=10)

def callback(data):
	cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
	orb = cv2.ORB()
	kp = orb.detect(cv_image,None)
	kp, des = orb.compute(cv_image, kp)
	img2 = cv2.drawKeypoints(cv_image,kp,color=(0,255,0), flags=0)
	
	image_message = CvBridge().cv2_to_imgmsg(img2, "bgr8")
	# plt.imshow(img2)
	# plt.show()
	
	pub.publish(image_message)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/camera/rgb/image_raw", Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()