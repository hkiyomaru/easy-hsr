import hsrb_interface
from hsrb_interface import ItemTypes

class BasicManager:
    def __init__(self):
        self.robot = hsrb_interface.Robot()
        self.omni_base = self.robot.get('omni_base')
        self.whole_body = self.robot.get('whole_body')
        self.gripper = self.robot.get('gripper')
        self.detector = self.robot.get('marker', self.robot.Items.OBJECT_DETECTION)
        self.tts = self.robot.try_get('default', ItemTypes.TEXT_TO_SPEECH)

if __name__ == '__main__':
    basic_manager = BasicManager()
