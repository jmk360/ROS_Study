#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def linstener():
    rospy.init_node('linstener', anonymous = True)
    sub = rospy.Subscriber('chatter', String, callback)
    rospy.spin()

def callback(data):
    print("I heard %s" %(data.data))

if __name__ == '__main__': 
    try:
        linstener()
    except rospy.ROSInterruptException:
        pass
