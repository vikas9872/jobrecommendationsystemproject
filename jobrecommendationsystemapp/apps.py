import os
import pickle
from django.apps import AppConfig

class JobrecommendationsystemappConfig(AppConfig):
    name = 'jobrecommendationsystemapp'

    def ready(self):
        models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
        try:
            with open(os.path.join(models_dir, 'tfidf_vectorizer.pkl'), 'rb') as f:
                self.tfidf_vectorizer = pickle.load(f)
            with open(os.path.join(models_dir, 'scaler.pkl'), 'rb') as f:
                self.scaler = pickle.load(f)
            with open(os.path.join(models_dir, 'onehot_encoder.pkl'), 'rb') as f:
                self.onehot_encoder = pickle.load(f)
            with open(os.path.join(models_dir, 'rf_classifier.pkl'), 'rb') as f:
                self.rf_classifier = pickle.load(f)
            with open(os.path.join(models_dir, 'jobdatasetform.pkl'), 'rb') as f:
                self.jobdatasetform = pickle.load(f)
            with open(os.path.join(models_dir, 'tfidf_vectorizer_resume.pkl'), 'rb') as f:
                self.tfidf_vectorizer_resume = pickle.load(f)
            with open(os.path.join(models_dir, 'rf_classifier_resume.pkl'), 'rb') as f:
                self.rf_classifier_resume = pickle.load(f)
            with open(os.path.join(models_dir, 'jobdatasetresume.pkl'), 'rb') as f:
                self.jobdatasetresume = pickle.load(f)
            print("✅ Model components loaded in AppConfig.")
        except Exception as e:
            print("❌ Failed to load model components:", e)