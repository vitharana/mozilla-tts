from TTS.api import TTS
import sounddevice as sd
import time
from file_handler import FileHandler

class TextSpeaker:
    def __init__(self, file_handler=None):
        self.tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
        self.sample_rate = self.tts.synthesizer.output_sample_rate
        self.file_handler = file_handler if file_handler else FileHandler()

    def read_text(self, text):
        if text:
            wav = self.tts.tts(text)
            sd.play(wav, self.sample_rate)
            sd.wait()

    def read_last_line(self):
        text = self.file_handler.get_last_line()
        if text:
            print(f"Reading: {text}")
            self.read_text(text)

    def read_all_new_lines(self):
        lines = self.file_handler.get_data()
        if lines:
            for line in lines:
                self.read_text(line)

    def run(self, interval=0.5):
        while True:
            self.read_last_line()
            time.sleep(interval)

    def run2(self, interval=0.5):
        while True:
            self.read_all_new_lines()
            time.sleep(interval)


# Usage
if __name__ == '__main__':
    speaker = TextSpeaker()
    speaker.run2()
