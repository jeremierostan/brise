import streamlit as st
import sounddevice as sd
import tempfile
from scipy.io.wavfile import write
import whisper
import numpy as np
if 'recording' not in st.session_state:
    st.session_state.recording = False

def start_recording():
    st.session_state.recording = True
    st.write("Recording started... Click 'Stop' to end.")
    return sd.rec(int(120 * 44100), samplerate=44100, channels=1, dtype='float64', blocking=False)

def stop_recording(recording):
    st.session_state.recording = False
    sd.stop()
    st.write("Converting speech to text...")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    write(temp_file.name, 44100, recording)
    return temp_file.name

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

# Streamlit UI
st.title("🗣️Brise")

if st.button('Start Recording') and not st.session_state.recording:
    st.session_state.audio_data = start_recording()

if st.button('Stop Recording') and st.session_state.recording:
    file_path = stop_recording(st.session_state.audio_data)
    transcription = transcribe_audio(file_path)
    st.text_area("Transcription", value=transcription, height=200)
