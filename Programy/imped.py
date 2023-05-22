import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# Parametry przechwytywania dźwięku
duration = 5  # Czas przechwytywania [s]
fs = 44100  # Częstotliwość próbkowania [Hz]

# Przechwytywanie dźwięku z karty dźwiękowej
print("Przechwytywanie dźwięku...")
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

# Obliczanie transformaty Fouriera
print("Obliczanie transformaty Fouriera...")
fft_data = np.fft.fft(audio_data[:, 0])
fft_freq = np.fft.fftfreq(len(fft_data), 1 / fs)

# Wykres widma
plt.figure()
plt.plot(fft_freq, np.abs(fft_data))
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo dźwięku")
plt.show()
