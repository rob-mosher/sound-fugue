import librosa
import numpy as np

class AnalysisModule:
    def __init__(self):
        self.pitch_sequence = None
        self.onset_times = None
    
    def analyze(self, audio_data, sample_rate):
        """Basic analysis of pitch and onset times"""
        # Extract pitch using librosa's pitch detection
        self.pitch_sequence = librosa.piptrack(y=audio_data, sr=sample_rate)[1]
        
        # Detect note onsets
        self.onset_times = librosa.onset.onset_detect(
            y=audio_data, sr=sample_rate, units='time'
        )
        
        return {
            'pitch_sequence': self.pitch_sequence,
            'onset_times': self.onset_times
        } 