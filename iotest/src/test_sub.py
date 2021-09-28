#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def listener():
    rospy.init_node('listener', anonymous = True)
    sub = rospy.Subscriber('chatter', String, callback)
    rospy.spin()

def callback(data):
    print("I heard %s" %(data.data))

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass