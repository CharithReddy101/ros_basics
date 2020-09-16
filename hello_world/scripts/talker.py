#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chat',String,queue_size=10)
    #tell ros that this is
    # publisher with topic name chatter and 
    #data type is string with queue size ie max char size is 10
    rospy.init_node('talker', anonymous = True) 
    #tell ros that this is a node with name talker and 
    #anonymous helps this node to be unique and avoids clashes with other nodes of same name
    rate = rospy.Rate(5) # 5 Hz 
    while not rospy.is_shutdown():
        msg_to_pub = "U There? %s" % rospy.get_time() 
        pub.publish(msg_to_pub)
        rospy.sleep(5)
if __name__ == '__main__':
    try: 
        talker() 
    except rospy.ROSInterruptException:
        pass