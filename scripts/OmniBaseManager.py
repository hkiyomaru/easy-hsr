 #!usr/bin/env python
import math
import sys

from BasicManager import BasicManager


class OmniBaseManager(BasicManager):
    def __init__(self):
        super(OmniBaseManager, self).__init__()

    def move_forward(self, distance=0.5, timeout=20.0):
        self.ready_to_go()
        self.omni_base.go(distance, 0.0, 0.0, timeout, relative=True)

    def move_backward(self, distance=0.5, timeout=20.0):
        self.ready_to_go()
        self.omni_base.go(-distance, 0.0, 0.0, timeout, relative=True)

    def turn_right(self, angle=90, timeout=20.0):
        angle = math.radians(angle)
        self.ready_to_go()
        self.omni_base.go(0.0, 0.0, -angle, timeout, relative=True)

    def turn_left(self, angle=90, timeout=20.0):
        angle = math.radians(angle)
        self.ready_to_go()
        self.omni_base.go(0.0, 0.0, angle, timeout, relative=True)


def main():
    omni_base_manager = OmniBaseManager()
    omni_base_manager.move_forward()
    return 0


if __name__ == '__main__':
    sys.exit(main())
