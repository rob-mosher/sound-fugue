import soundfile as sf
import numpy as np

class OutputModule:
    def __init__(self):
        self.combined_output = None
    
    def combine_and_save(self, original_audio, counterpoint, sample_rate, output_path):
        """Combine original and counterpoint, then save to file"""
        # Normalize and combine the signals
        self.combined_output = original_audio + counterpoint
        
        # Normalize to prevent clipping
        self.combined_output = self.combined_output / np.max(np.abs(self.combined_output))
        
        # Save to file
        sf.write(output_path, self.combined_output, sample_rate) 