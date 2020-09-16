#!/usr/bin/env python
import rospy #importing rospy
from std_msgs.msg import String #importing String type from standard msgs

def callback(received_data):  #callback function should be defined 
    rospy.loginfo(rospy.get_caller_id() + '%s Yupp ', received_data.data)


def listener(): 
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('chat', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    rospy.sleep(1)