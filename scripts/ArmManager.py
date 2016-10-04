#!usr/bin/env python
import roslib
import rospy
import trajectory_msgs.msg
import controller_manager_msgs.srv

import sys


class ArmManager():
    def __init__(self):
        self.pub = rospy.Publisher('/hsrb/arm_trajectory_controller/command', trajectory_msgs.msg.JointTrajectory, queue_size=10)
        self.running = False
        self.establish_connection()


    def moveto(self, destination, relation='relative'):
        if relation is 'relative':
            self.move_relatively(destination)
        elif relation is 'absolute':
            self.move_absolutely(destination)
        else:
            print "Invalid relation:", relation
            sys.exit(1)

    def move_relatively(self, destination):
        trajectory = trajectory_msgs.msg.JointTrajectory()
        trajectory.joint_names = ["arm_lift_joint", "arm_flex_joint", "arm_roll_joint", "wrist_flex_joint", "wrist_roll_joint"]
        p = trajectory_msgs.msg.JointTrajectoryPoint()
        p.positions = destination["positions"]
        p.velocities = destination["velocities"]
        p.time_from_start = rospy.Time(3)
        trajectory.points = [p]
        self.pub.publish(trajectory)

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
    rospy.init_node('arm_test')
    destination = {
        "positions": [0, -1.5, 0, 0, 0],
        "velocities": [0, 0, 0, 0, 0]
    }
    arm_manager = ArmManager()
    arm_manager.moveto(destination=destination)
    return 0


if __name__ == '__main__':
    sys.exit(main())
