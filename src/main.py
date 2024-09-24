from src.camera import initialize_camera, capture_frame, release_camera
from src.object_detection import ObjectDetector
from src.voice_command import listen_command, speak
from src.weed_removal_logic import WeedRemovalLogic
from src.intent_detection import IntentDetector
from src.active_learning import ActiveLearning

def main():
    camera = initialize_camera()
    object_detector = ObjectDetector()
    weed_removal_logic = WeedRemovalLogic()
    intent_detector = IntentDetector()

    # Sample commands for training intent detector
    commands = ["start", "stop", "cut", "avoid"]
    labels = ["start", "stop", "cut", "avoid"]
    intent_detector.train_intent_model(commands, labels)

    try:
        while True:
            command = listen_command()
            intent = intent_detector.predict_intent(command)

            if intent == "start":
                speak("Starting weed detection")
                while True:
                    frame = capture_frame(camera)
                    if frame is None:
                        continue

                    predictions = object_detector.predict(frame)
                    classification = object_detector.classify(predictions)
                    weed_removal_logic.process_decision(classification)

                    # Break from loop if user says stop


                    if listen_command() == "stop":
                        break

            elif intent == "stop":
                speak("Stopping the robot")
                break

    finally:
        release_camera(camera)

if __name__ == "__main__":
    main()