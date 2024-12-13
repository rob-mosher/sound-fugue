# sound-fugue

SoundFugue: A generative sound exploration blending counterpoint and harmony, inspired by the structure of a musical fugue.

## Setup

1. Ensure you have Python 3.13 installed
   ```bash
   pyenv install 3.13
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the project
   ```bash
   python src/main.py input.wav
   # Or specify output file:
   python src/main.py input.wav -o output.wav
   ```

5. When done, deactivate virtual environment
   ```bash
   deactivate
   ```

