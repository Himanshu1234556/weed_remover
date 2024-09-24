import cv2
import numpy as np
from tensorflow.keras.models import load_model

class ObjectDetector:
    def __init__(self, model_path='models/latest_model.h5'):
        self.model = load_model(model_path)

    def preprocess_image(self, image):
        resized_image = cv2.resize(image, (224, 224))
        normalized_image = resized_image / 255.0
        return np.expand_dims(normalized_image, axis=0)

    def predict(self, frame):
        processed_frame = self.preprocess_image(frame)
        predictions = self.model.predict(processed_frame)
        return predictions

    def classify(self, predictions):
        weed_index = 0  # Assuming weed is at index 0
        crop_index = 1  # Assuming crop is at index 1
        if predictions[0][weed_index] > 0.5:  # 50% confidence threshold
            return "weed"
        elif predictions[0][crop_index] > 0.5:
            return "crop"
        return "unknown"