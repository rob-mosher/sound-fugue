import sys
import argparse
from pathlib import Path

# Verify Python version at runtime
REQUIRED_PYTHON = (3, 13)
if sys.version_info < REQUIRED_PYTHON:
    sys.exit(f"Python {'.'.join(str(n) for n in REQUIRED_PYTHON)} or later is required.")

from input_module import InputModule
from analysis_module import AnalysisModule
from counterpoint_module import CounterpointModule
from output_module import OutputModule

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate counterpoint from audio file')
    parser.add_argument('input_file', type=str, help='Path to input audio file (WAV format)')
    parser.add_argument('--output', '-o', type=str, default='output.wav',
                       help='Path for output file (default: output.wav)')
    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        sys.exit(f"Error: Input file '{input_path}' does not exist")
    
    # Initialize modules
    input_mod = InputModule()
    analysis_mod = AnalysisModule()
    counterpoint_mod = CounterpointModule()
    output_mod = OutputModule()
    
    try:
        # Process audio
        audio_data, sample_rate = input_mod.load_audio(str(input_path))
        
        # Analyze
        analysis_data = analysis_mod.analyze(audio_data, sample_rate)
        
        # Generate counterpoint
        counterpoint = counterpoint_mod.generate_counterpoint(analysis_data)
        
        # Output
        output_mod.combine_and_save(
            audio_data,
            counterpoint,
            sample_rate,
            args.output
        )
        print(f"Successfully generated counterpoint: {args.output}")
        
    except Exception as e:
        sys.exit(f"Error processing audio: {str(e)}")

if __name__ == "__main__":
    main() 