# This module is based using Whisper AI and Voice Recoder to produce
# README.MD for instructions and how to use.
import pyaudio
import wave
import os
def voice_record():
    audio = pyaudio.PyAudio()

    # Sound Stream
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    frames = []

    try:
        while True:
            data = stream.read(1024)
            frames.append(data)

    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open("myrecording.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    print('end')

voice_record()
