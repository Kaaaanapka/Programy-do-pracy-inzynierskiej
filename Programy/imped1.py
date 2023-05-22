import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Parametry obwodu RC
R = 10  # Rezystancja [Ohm]
C = 1e-6  # Pojemność [Farad]

# Tworzenie częstotliwości
frequencies = np.logspace(-1, 5, num=50)  # Przykładowe częstotliwości (uwzględniające 0 Hz)

# Pobieranie próbek z karty dźwiękowej
duration = 1.0  # Czas trwania nagrania [s]
sample_rate = 44100  # Częstotliwość próbkowania [Hz]
samples = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()

# Obliczanie impedancji teoretycznej
Z_theoretical = R / (1 + 1j * 2 * np.pi * frequencies * R * C)

# Przetwarzanie pobranych próbek
Z_measured = np.fft.fft(samples.flatten())
frequencies_measured = np.fft.fftfreq(len(samples), d=1/sample_rate)

# Wyświetlanie wyników
print("Parametry obwodu RC:")
print("R =", R)
print("C =", C)

# Wykres Nyquista
plt.figure()
plt.plot(Z_measured.real, -Z_measured.imag, "o", label="Pomiar")
plt.plot(Z_theoretical.real, -Z_theoretical.imag, label="Teoria")
plt.xlabel("Re(Z)")
plt.ylabel("-Im(Z)")
plt.legend()
plt.show()
