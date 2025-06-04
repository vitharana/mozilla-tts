import requests
import sounddevice as sd
import soundfile as sf
import io
import time

class TextSpeakerRemote:
    def __init__(self, host="localhost", port=5002):
        self.url = f"http://{host}:{port}/api/tts"

    def read_text(self, text):
        if text:
            response = requests.get(self.url, params={"text": text})
            if response.status_code == 200:
                wav_bytes = io.BytesIO(response.content)
                data, samplerate = sf.read(wav_bytes)
                sd.play(data, samplerate)
                sd.wait()
            else:
                print("TTS server error:", response.status_code)


speaker = TextSpeakerRemote()
speaker.read_text("I am Sandun")
speaker.read_text("I am Sandun")
t = time.time()
speaker.read_text("I am Sandun")
print((time.time() - t))
speaker.read_text("I am Sandun")
speaker.read_text("I am Sampath")