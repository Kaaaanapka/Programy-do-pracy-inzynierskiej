import numpy as np
import sounddevice as sd

# Parametry pomiaru
duration = 5  # Czas trwania pomiaru [s]
sample_rate = 44100  # Częstotliwość próbkowania [Hz]
frequency = 10  # Częstotliwość sygnału testowego [Hz]
amplitude = 0.5  # Amplituda sygnału testowego

# Funkcja obsługująca przetwarzanie próbek audio
def callback(indata, frames, time, status):
    # Tutaj można przetwarzać próbki audio w czasie rzeczywistym
    # Można wykonywać obliczenia, analizować widmo, dopasowywać modele itp.
    pass

# Konfiguracja karty dźwiękowej
sd.default.samplerate = sample_rate
sd.default.channels = 1  # Jeden kanał (mono)

# Generowanie sygnału testowego
t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Rozpoczęcie pomiaru
with sd.InputStream(callback=callback):
    sd.play(signal, samplerate=sample_rate)
    sd.wait()

# Tutaj można przetwarzać zebrane dane, dopasować modele teoretyczne itp.
# Można korzystać z bibliotek takich jak NumPy, SciPy do analizy sygnałów

# Przykładowa analiza danych - wyliczenie widma sygnału
spectrum = np.abs(np.fft.fft(signal))

# Wyświetlanie wyników
import matplotlib.pyplot as plt

# Wykres sygnału testowego
plt.figure()
plt.plot(t, signal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Sygnał testowy")
plt.show()

# Wykres widma sygnału
freq = np.fft.fftfreq(len(t), d=1/sample_rate)
plt.figure()
plt.plot(freq[:len(freq)//2], spectrum[:len(freq)//2])
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo sygnału")
plt.show()
