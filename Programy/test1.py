import numpy as np
import sounddevice as sd
import csv

A = float(input("Określ wielkość amplitudy: "))  # amplituda
f_start = float(input("Określ początkową wartość częstotliwości: "))  # początkowa częstotliwość
f_end = float(input("Określ końcową wartość częstotliwości: "))  # końcowa częstotliwość
phi = 0  # faza
sr = 44100  # częstotliwość próbkowania
duration = 4  # czas trwania w sekundach
repetitions = 20  # liczba powtórzeń

# Podzielenie amplitudy przez 2
A /= 2

# Generowanie kolejnych wartości częstotliwości
frequencies = np.linspace(f_start, f_end, repetitions)

# Lista do przechowywania wyników impedancji
impedance_results = []

for freq in frequencies:
    time = np.arange(0, 1/freq, 1/sr)
    y = A * np.sin(2 * np.pi * freq * time + phi)

    RC_constant = 1 / (2 * np.pi * freq)  # stała czasowa RC

    # Symulacja obwodu RC
    filtered_signal = np.zeros_like(y)
    for i in range(1, len(y)):
        filtered_signal[i] = (1 - 1 / sr / RC_constant) * filtered_signal[i-1] + y[i] / sr / RC_constant

    signal = np.tile(filtered_signal, int(sr / freq))
    total_duration = len(signal) / sr

    if total_duration < duration:
        num_repetitions = int(np.ceil(duration / total_duration))
        signal = np.tile(signal, num_repetitions)

    signal = signal[:int(sr * duration)]

    # Odtwarzanie sygnału z połączenia RC
    sd.play(signal, sr, blocking=True)

    # Nagrywanie dźwięku z mikrofonu
    recording = sd.rec(int(duration * sr), samplerate=sr, channels=1)
    sd.wait()

    # Obliczanie impedancji EIS na podstawie amplitudy sygnału
    amplitude = np.max(np.abs(recording))
    impedance = A / amplitude

    # Obliczanie impedancji rzeczywistej i urojonej
    impedance_real = np.real(impedance)
    impedance_imag = np.imag(impedance)

    # Dodawanie wyniku do listy
    impedance_results.append((freq, impedance_real, impedance_imag))


# Zapisywanie wartości do pliku CSV
filename = 'impedancja_eis.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Częstotliwość', 'Impedancja Rzeczywista', 'Impedancja Urojona'])
    for freq, impedance_real, impedance_imag in impedance_results:
        writer.writerow([freq, impedance_real, impedance_imag])

print(f"Dane zapisano do pliku: {filename}")
