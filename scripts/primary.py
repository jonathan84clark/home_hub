#!/usr/bin/env python
#################################################################
# PRIMARY
# DESC: The primary node is the first node created for the home hub
# system.
# Author: Jonathan L Clark
# Date: 5/28/2020
##################################################################
from threading import Thread
import json
import rospy

##############################################################
# SERVER FUNCTIONS
##############################################################
#@app.route('/')
#def index():
#    return redirect('/data.json')


#@app.route('/handle_post', methods=['GET', 'POST'])
#def add_waypoint():
#
#    return "Done"

# Primary node for the Qurrent ROS system
class PrimaryNode():
    def __init__(self):
        pass


if __name__ == "__main__":
    rospy.init_node('Primary', anonymous=True)
    rospy.loginfo("Started primary node!")
    primary_node = PrimaryNode()
    rospy.spin() 