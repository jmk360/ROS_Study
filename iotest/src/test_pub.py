#!/usr/bin/env python

import rospy
from rospy.exceptions import ROSInterruptException
from std_msgs.msg import String

def talker():
    rospy.init_node('talker', anonymous = True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(1) # 1hz => 1s

    while not rospy.is_shutdown():
        hello_str = 'hello world %s' %(rospy.get_time())
        print(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except ROSInterruptException:
        pass