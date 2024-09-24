from src.robot_controller import RobotController
from src.speak import speak

class WeedRemovalLogic:
    def __init__(self):
        self.controller = RobotController()

    def process_decision(self, classification):
        if classification == "weed":
            self.controller.cut_weed()
        elif classification == "crop":
            self.controller.avoid_crop()
        else:
            speak("Unknown classification.")