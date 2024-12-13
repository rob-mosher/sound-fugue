import librosa
import numpy as np

class InputModule:
    def __init__(self):
        self.audio_data = None
        self.sample_rate = None
    
    def load_audio(self, file_path):
        """Load audio file using librosa"""
        self.audio_data, self.sample_rate = librosa.load(file_path)
        return self.audio_data, self.sample_rate 