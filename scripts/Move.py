#!usr/bin/env python
import roslib
import rospy
import trajectory_msgs.msg
import controller_manager_msgs.srv

import sys


class Move():
    def __init__(self):
        self.pub = rospy.Publisher('/hsrb/omni_base_controller/command', trajectory_msgs.msg.JointTrajectory, queue_size=10)
        self.establish_connection()

    def __call__(self, destination, relation='relative'):
        # Move to the destination
        if relation is 'relative':
            self.move_relatively(destination)
        elif relation is 'absolute':
            self.move_absolutely(destination)
        else:
            print "Invalid relation:", relation
            sys.exit(1)

    def move_relatively(self, destination):
        traj = trajectory_msgs.msg.JointTrajectory()
        traj.joint_names = ["odom_x", "odom_y", "odom_t"]
        p = trajectory_msgs.msg.JointTrajectoryPoint()
        p.positions = destination["positions"]
        p.velocities = destination["velocities"]
        p.time_from_start = rospy.Time(6)
        traj.points = [p]
        self.pub.publish(traj)

    def move_absolutely(self, destination):
        pass

    def establish_connection(self):
        while self.pub.get_num_connections() == 0 and not rospy.is_shutdown():
            rospy.sleep(0.1)
        rospy.wait_for_service('/hsrb/controller_manager/list_controllers')
        list_controllers = rospy.ServiceProxy('/hsrb/controller_manager/list_controllers', controller_manager_msgs.srv.ListControllers)
        running = False
        while running == False and not rospy.is_shutdown():
            rospy.sleep(0.1)
            for c in list_controllers().controller:
                if c.name == 'omni_base_controller' and c.state == 'running':
                    running = True


def main():
    rospy.init_node('move_test')
    destination = {
        "positions": [1, 0, 0],
        "velocities": [0, 0, 0]
    }
    move = Move()(destination=destination)
    return 0


if __name__ == '__main__':
    sys.exit(main())
