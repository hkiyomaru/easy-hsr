#!usr/bin/env python
import sys

from BasicManager import BasicManager


class ArmManager(BasicManager):
    def __init__(self):
        super(ArmManager, self).__init__()

    def move_to_target(self, tf):
        whole_body.move_end_effector_pose(geometry.pose(z=-0.02, ek=-1.57), 'ar_marker/503')

def main():
    arm_manager = ArmManager()
    return 0


if __name__ == '__main__':
    sys.exit(main())
