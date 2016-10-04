#!usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg
import controller_manager_msgs.srv

import sys


class OmniBaseManager():
    def __init__(self):
        self.pub = rospy.Publisher('/hsrb/command_velocity', geometry_msgs.msg.Twist, queue_size=10)
        self.running = False
        self.establish_connection()

    def goto(self, destination, relation='relative'):
        if relation is 'relative':
            self.move_relatively(destination)
        elif relation is 'absolute':
            self.move_absolutely(destination)
        else:
            print "Invalid relation:", relation
            sys.exit(1)

    def move_relatively(self, destination):
        twist = geometry_msgs.msg.Twist()
        twist.linear.x = destination["linear"]["x"]
        twist.linear.y = destination["linear"]["y"]
        twist.linear.z = destination["linear"]["z"]
        twist.angular.x = destination["angular"]["x"]
        twist.angular.y = destination["angular"]["y"]
        twist.angular.z = destination["angular"]["z"]
        self.pub.publish(twist)

    def move_absolutely(self, destination):
        pass

    def establish_connection(self):
        while self.pub.get_num_connections() == 0 and not rospy.is_shutdown():
            rospy.sleep(0.1)
        rospy.wait_for_service('/hsrb/controller_manager/list_controllers')
        list_controllers = rospy.ServiceProxy('/hsrb/controller_manager/list_controllers', controller_manager_msgs.srv.ListControllers)
        while self.running == False and not rospy.is_shutdown():
            rospy.sleep(0.1)
            for c in list_controllers().controller:
                if c.name == 'omni_base_controller' and c.state == 'running':
                    self.running = True

    def isRunning(self):
        return self.running


def main():
    rospy.init_node('move_test')
    destination = {
        "linear": {
            "x": 1.0,
            "y": 0.0,
            "z": 0.0,
        },
        "angular": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0,
        }
    }
    omni_base_manager = OmniBaseManager()
    omni_base_manager.goto(destination=destination)
    return 0


if __name__ == '__main__':
    sys.exit(main())
