import whisper
import os
from pydub import AudioSegment

def convert_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.rsplit('.', 1)[0] + '.wav'
    audio.export(wav_path, format="wav")
    return wav_path

def split_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_file(file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_path = f"{file_path.rsplit('.', 1)[0]}_chunk_{i // chunk_length_ms}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)
    return chunks

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return
    
    try:
        # Convert to WAV if necessary
        if not file_path.endswith('.wav'):
            file_path = convert_to_wav(file_path)
        
        # Load the Whisper model
        model = whisper.load_model("base")
        
        # Split and transcribe chunks
        chunks = split_audio(file_path)
        full_transcription = ""
        
        for chunk in chunks:
            result = model.transcribe(chunk)
            full_transcription += result["text"] + "\n"
        
        # Print the transcription
        print("Transcription: ", full_transcription)
        
        # Save the transcription to a file
        save_transcription(full_transcription, file_path.rsplit('.', 1)[0] + '.txt')
        
        return full_transcription
    except Exception as e:
        print(f"An error occurred during transcription: {e}")

def save_transcription(text, output_path):
    with open(output_path, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py path_to_audio_file")
        sys.exit(1)
    
    file_path = sys.argv[1]
    transcribe_audio(file_path)