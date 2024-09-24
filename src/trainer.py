import os
import cv2
import numpy as np
import tensorflow as tf

class ModelTrainer:
    def load_data(self, images_folder):
        images = []
        labels = []
        
        for label in os.listdir(images_folder):
            label_folder = os.path.join(images_folder, label)
            for img_name in os.listdir(label_folder):
                img_path = os.path.join(label_folder, img_name)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (224, 224))
                images.append(img)
                labels.append(label)
        
        return np.array(images), np.array(labels)

    def train_model(self):
        X, y = self.load_data('data')
        
        # Encode labels
        from sklearn.preprocessing import LabelEncoder
        encoder = LabelEncoder()
        y_encoded = encoder.fit_transform(y)

        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(len(set(y)), activation='softmax')  # Number of classes
        ])
        
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
        model.fit(X, y_encoded, epochs=10)
        model.save('models/latest_model.h5')

if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.train_model()