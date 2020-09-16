#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float64

rospy.init_node('move_rrbot')

pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=1)
pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=1)

rate = rospy.Rate(1)  
rot1 = 1.5
rot2 =1
# rot.linear.x = 0.2

while not rospy.is_shutdown():
    pub1.publish(rot1)
    pub2.publish(rot2)
    rate.sleep()

    