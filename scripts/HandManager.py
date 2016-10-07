#!usr/bin/env python
import sys

from BasicManager import BasicManager

class HandManager(BasicManager):
    def __init__(self):
        super(HandManager, self).__init__()

    def grasp(self):
        self.gripper.command(0.0)

    def open(self):
        self.gripper.command(1.2)

def main():
    hand_manager = HandManager()
    hand_manager.grasp()
    return 0


if __name__ == '__main__':
    sys.exit(main())
