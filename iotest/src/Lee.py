#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from pubsub_example1 import ros_chat_test

if __name__ == '__main__':
    try:
        chat_classing = ros_chat_test('Lee', 'Park', 'Kim', 'Hog')
    except rospy.ROSInterruptException:
        pass