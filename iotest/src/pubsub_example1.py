#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class ros_chat_test:
    def __init__(self, nodeName, listen_1, listen_2, listen_3):
        rospy.init_node('ChatNode'+nodeName, anonymous=True)
        self.listen_1 = listen_1
        self.listen_2 = listen_2
        self.listen_3 = listen_3
        pub = rospy.Publisher(nodeName, String, queue_size=10)
        sub_1 = rospy.Subscriber(self.listen_1, String, self.callback_1)
        sub_2 = rospy.Subscriber(self.listen_2, String, self.callback_2)
        sub_3 = rospy.Subscriber(self.listen_3, String, self.callback_3)
        rate = rospy.Rate(1) # 1hz => 1s

        while not rospy.is_shutdown():
            out_str = input('%s: '%(nodeName))
            pub.publish(out_str)

    def callback_1(self, data):
        print('%s: %s'%(self.listen_1, data.data))

    def callback_2(self, data):
        print('%s: %s'%(self.listen_2, data.data))

    def callback_3(self, data):
        print('%s: %s'%(self.listen_3, data.data))

if __name__ == '__main__':
    try:
        chat_classing = ros_chat_test('Kim', 'Park', 'Lee', 'Hog')
    except rospy.ROSInterruptException:
        pass