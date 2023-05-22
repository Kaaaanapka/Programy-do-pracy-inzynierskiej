import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

# Wczytaj plik dźwiękowy
sample_rate, data = wavfile.read('probka.wav')

# Oblicz widmo dźwiękowe
fft_data = np.fft.fft(data)

# Oblicz częstotliwości odpowiadające próbkowaniu
freqs = np.fft.fftfreq(len(data), 1/sample_rate)

# Wyświetl widmo dźwiękowe
plt.plot(freqs, np.abs(fft_data))
plt.xlabel('Częstotliwość (Hz)')
plt.ylabel('Amplituda')
plt.title('Widmo dźwiękowe')
plt.show()
