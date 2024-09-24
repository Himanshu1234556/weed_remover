from src.utils import load_training_data
from src.speak import speak

class ActiveLearning:
    def __init__(self, model):
        self.model = model

    def request_feedback(self, frame, predicted_label):
        speak(f"Predicted: {predicted_label}. Do you want to correct it? Say yes or no.")
        feedback = input()
        if feedback.lower() == 'yes':
            correct_label = input("Enter the correct label (weed/crop): ")
            # Log the feedback
            speak(f"Logging the correction for {predicted_label} to {correct_label}.")
            # Log action could be removed if logging is not needed

    def retrain_model(self):
        training_data = load_training_data()
        # Retrain the model using the newly added data
        # (Implementation of retraining logic will depend on your model architecture)