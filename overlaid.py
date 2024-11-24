from pydub import AudioSegment


filename = f"speaker-audio.wav"
audio = AudioSegment.from_wav(filename)
background_music = AudioSegment.from_wav("noise.wav")

background_music = background_music - 10

background_music = background_music[:len(audio)]

combined = audio.overlay(background_music)

fn = f"audio-attack.wav"
combined.export(fn, format="wav")
