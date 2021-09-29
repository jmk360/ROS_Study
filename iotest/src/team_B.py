#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talk_listen():
    rospy.init_node('talk_B', anonymous = True)
    pub = rospy.Publisher('chat_B', String, queue_size=10)
    sub_A = rospy.Subscriber('chat_A', String, callback_A)
    sub_C = rospy.Subscriber('chat_C', String, callback_C)
    sub_D = rospy.Subscriber('chat_D', String, callback_D)
    rate = rospy.Rate(1) # 1hz => 1s

    while not rospy.is_shutdown():
        out_str = str(input("B: "))
        pub.publish(out_str)

def callback_A(data):
    print('A: %s' %(data.data))

def callback_C(data):
    print('C: %s' %(data.data))

def callback_D(data):
    print('D: %s' %(data.data))

if __name__ == '__main__':
    try:
        talk_listen()
    except rospy.ROSInterruptException:
        pass