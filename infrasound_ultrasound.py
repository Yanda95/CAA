import numpy as np
import soundfile as sf
from pydub import AudioSegment
from pydub.generators import WhiteNoise, Sine

filename = f"speaker-audio.wav"
speak_audio = AudioSegment.from_wav(filename)

def generate_infrasound():
    low_freq_tone = Sine(10).to_audio_segment(duration=len(speak_audio))

def generate_ultrasonic_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone

def save_to_wav(filename, data, sample_rate):
    sf.write(filename, data, sample_rate)

duration = 5
sample_rate = 44100
frequency = 22000

ultrasonic_noise = generate_ultrasonic_tone(frequency, duration, sample_rate)

save_to_wav("ultrasonic_noise.wav", ultrasonic_noise, sample_rate)
