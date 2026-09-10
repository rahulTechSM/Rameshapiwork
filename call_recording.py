import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate

seconds = int(input("Enter recording duration (seconds): "))

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()

write("RahulTest.wav", fs, recording)
print("Saved as RahulTest.wav")