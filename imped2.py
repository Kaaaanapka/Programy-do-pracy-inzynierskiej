import numpy as np
import sounddevice as sd
from scipy.fftpack import fft
import matplotlib.pyplot as plt

def generate_signal(frequency, duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal

def record_audio(duration, sampling_rate):
    recording = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1, blocking=True)
    return recording.flatten()

def perform_fft(signal):
    fft_result = fft(signal)
    return np.abs(fft_result)

def calculate_amplitude_ratio(input_signal, output_signal):
    return np.divide(output_signal, input_signal)

def plot_signal(signal, sampling_rate, title):
    duration = len(signal / sampling_rate)
    time = np.linspace(0, duration, len(signal))
    plt.figure()
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel("Czas (s)")
    plt.ylabel("Amplituda")
    plt.show()

def plot_fft (fft_result, sampling_rate, title):
    duration = len(fft_result) / sampling_rate
    freq = np.linspace(0, 1 / ( 2 *duration), len (fft_result) // 2 )
    plt.figure()
    plt.plot(freq, np.abs(fft_result[:len(fft_result) //2]))
    plt.title(title)
    plt.xlabel("Czestotliwosc (Hz)")
    plt.ylabel("Amplituda")
    plt.show()

def main():
    # Parametry sygnału
    frequencies = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000,
                    14000, 15000, 16000, 17000, 18000, 19000, 20000]  # Przykładowe częstotliwości
    duration = 1.0
    sampling_rate = 44100

    for frequency in frequencies:
        # Generowanie sygnału
        signal = generate_signal(frequency, duration, sampling_rate)

        # Nagrywanie dźwięku z mikrofonu
        recorded_signal = record_audio(duration, sampling_rate)

        # Obliczanie FFT
        fft_input = perform_fft(signal)
        fft_output = perform_fft(recorded_signal)

        # Dzielenie amplitudy FFT wyjścia przez FFT wejścia
        amplitude_ratio = calculate_amplitude_ratio(fft_input, fft_output)

        print(f"Amplituda FFT wyjścia / FFT wejścia dla częstotliwości {frequency} Hz:")
        print(amplitude_ratio)



        plot_signal(signal, sampling_rate,  f"Teoretyczny sygnal - {frequency} Hz")
        plot_signal(recorded_signal, sampling_rate, f"Nagrany sygnal - {frequency} Hz")
        plot_signal(amplitude_ratio, sampling_rate,  f"Amplituda FFT wyjścia / FFT wejścia dla częstotliwości - {frequency} Hz")
        plot_fft(fft_input, sampling_rate, f"FFT wejscie - {frequency} Hz")
        plot_fft(fft_output, sampling_rate, f"FFT wyjscie - {frequency} Hz")
        
if __name__ == "__main__":
    main()
