#!usr/bin/env python
import sys

from BasicManager import BasicManager


_BOTTLE_TF='ar_marker/503'


class DetectARMarkerManager(BasicManager):
    def __init__(self):
        super(DetectARMarkerManager, self).__init__()

    def find_ar_marker(self):
        objects = self.detector.get_objects()
        return objects

def main():
    detect_ar_marler_manager = DetectARMarkerManager()
    print detect_ar_marler_manager.find_ar_marker()
    return 0


if __name__ == '__main__':
    sys.exit(main())
