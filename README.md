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

Transcription Instructions

1. Place Your Audio File in a Known Directory

Ensure your audio file is in a directory that you can easily access.

2. Run the Script with the New Audio File Path

Use the following command to run the transcription script, specifying the path to your new audio file.
For example, if your audio file is named new_audio.m4a and located in /Users/xxxx/Documents/New_Audio/, you would run:
python transcribe.py /Users/xxxx/Documents/New_Audio/new_audio.m4a

Example Process

	1.	Open VS Code Terminal or Terminal on your Mac.
	2.	Navigate to your project directory:
      cd /Users/abraar/Documents/transcribe

 	3.	Activate the virtual environment (if not already activated):
      cd /Users/xxx/Documents/transcribe
	4.	Run the script with the path to the new audio file:
      python transcribe.py /Users/abraar/Documents/New_Audio/new_audio.m4a

General Usage

The general usage of the script is:
python transcribe.py path_to_audio_file

