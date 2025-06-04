from speech_engine import TextSpeaker
import time

speaker = TextSpeaker()
speaker.read_text("hey how are you")

speaker.read_text("hey how are you")



speaker.read_text("I am Sandun")
speaker.read_text("I am Sandun")
t = time.time()
speaker.read_text("I am Sandun")
print((time.time() - t))
speaker.read_text("I am Sandun")
speaker.read_text("I am Sampath")