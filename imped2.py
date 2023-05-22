import numpy as np
import sounddevice as sd
from scipy.fftpack import fft

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

def main():
    # Parametry sygnału
    frequencies = [1000, 2000, 5000]  # Przykładowe częstotliwości
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

if __name__ == "__main__":
    main()
