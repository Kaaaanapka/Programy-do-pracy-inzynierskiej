import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt


time_step = 0.05
time_vec = np.arange(0, 10, time_step)
period = 5
sig = (np.sin(2*np.pi*time_vec/period) + np.random.randn(time_vec.size))

sig_fft = fftpack.fft(sig)

Amplitude = np.abs(sig_fft)
Power = Amplitude**2
np.angle(sig_fft)

sample_freq = fftpack.fftfreq(sig.size, d=time_step)

Amp_freq = np.array([Amplitude, sample_freq])

Amp_position = Amp_freq[0,:].argmax()

peak_freq = Amp_freq[1, Amp_position]

high_freq_fft = sig_fft.copy()
high_freq_fft [np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

#fig, ax = plt_subplots()
#plt.plot(filtered_sig, ax=ax)
#plt.plot(high_freq_fft, ax=ax)

plt.figure(figsize=(15, 5))
plt.plot(filtered_sig, high_freq_fft )

plt.ylabel('Fala dźwieku')
plt.xlabel('Czas (w s)')
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
plt.title('ScipyFFT')

plt.show()