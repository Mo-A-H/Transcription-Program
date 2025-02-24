Whisper API - Transcription Program Setup  
==========================================

This guide provides step-by-step instructions to install and set up OpenAI's Whisper API  
for transcribing audio files.

1. Prerequisites
Ensure you have **Python 3.8 or later** installed.  
Check your version with:  
```sh
python --version

2. Create a Virtual Environment 
source whisper_env/bin/activate

3. Upgrade Pip & Install Required Dependencies
pip install --upgrade pip setuptools wheel

4. Install Whisper and Dependencies
pip install openai-whisper
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ffmpeg-python

5. Install FFmpeg(mac)
brew install ffmpeg

6. Verify Installation
whisper --help

