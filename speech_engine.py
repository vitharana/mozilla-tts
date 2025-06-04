from TTS.api import TTS
import sounddevice as sd
import numpy as np
import time
from file_handler import FileHandler

# Initialize TTS with a pretrained model (this downloads if needed)
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
sr = tts.synthesizer.output_sample_rate

# Initialize FileHandler
file = FileHandler()

def read_text(text):
    if text:
        wav = tts.tts(text)
        sd.play(wav, sr)
        sd.wait()

def read_last_line_from_file(file_handler):
    text = file_handler.get_last_line()
    if text:
        print(f"Reading: {text}")
        read_text(text)

def main():
    while True:
        read_last_line_from_file(file)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
