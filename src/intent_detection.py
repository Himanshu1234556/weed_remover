from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class IntentDetector:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train_intent_model(self, commands, labels):
        X = self.vectorizer.fit_transform(commands)
        self.model.fit(X, labels)

    def predict_intent(self, command):
        X = self.vectorizer.transform([command])
        prediction = self.model.predict(X)
        return prediction[0]