 #!usr/bin/env python
import sys

from BasicManager import BasicManager


class BodyManager(BasicManager):
    def __init__(self):
        super(BodyManager, self).__init__()
        self.management_joint = 'arm_lift_joint'
        self.joint_limits = self.limits_of_position(self.management_joint)

    def up(self, height=0.2):
        current_position = self.current_position(self.management_joint)
        height = min(current_position + height, self.joint_limits[1])
        self.whole_body.move_to_joint_positions({'arm_lift_joint': height})

    def down(self, height=0.2):
        current_position = self.current_position(self.management_joint)
        height = max(current_position - height, self.joint_limits[0])
        self.whole_body.move_to_joint_positions({'arm_lift_joint': height})

def main():
    body_manager = BodyManager()
    body_manager.down()
    return 0


if __name__ == '__main__':
    sys.exit(main())
