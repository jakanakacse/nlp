import speech_recognition as sr
import os

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    if not os.path.exists(audio_path):
        return f"Audio file '{audio_path}' not found. Please provide a valid .wav file."

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Recognition service error: {e}"

sample_audio = "sample.wav"
print(f"--- Automatic Speech Recognition (ASR) ---")
print(f"Processing audio file: {sample_audio}")
text = transcribe_audio(sample_audio)
print(f"Transcribed Text: {text}")

