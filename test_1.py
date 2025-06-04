from TTS.api import TTS
import sounddevice as sd
import numpy as np

# Initialize TTS with a pretrained model (this downloads if needed)
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")

# Synthesize speech to numpy array
text_samples = ["hey how are you", "how old are you", "where do you live", "he is tall"]


for sample in text_samples:


    wav = tts.tts(sample)

    # Get sample rate (usually 22050 or 24000 depending on model)
    sr = tts.synthesizer.output_sample_rate

    # Play audio directly from numpy array
    sd.play(wav, sr)
    sd.wait()
    print("done")
