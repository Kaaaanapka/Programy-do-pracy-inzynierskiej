import numpy as np
import matplotlib.pyplot as plt

#tworzenie sygnału

Fs = 2000 #próbkowanie czestotliwosc
ts = 1 / Fs # czas probkowania interval
f0 = 100 # czestotliwosc sygnału

N = int(10* Fs / f0) #wartosc pod 1 zamist 10

t = np.linspace (0, (N-1)*ts, N) #time steps
fstep = Fs/ N #czestotliwosc interval
f = np.linspace(0, (N-1)*fstep, N) #freq steps

y = 1 * np.sin(2 * np.pi * f0 * t)

# FFT

X = np.fft.fft(y)
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_mag_plot = 2*X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0] / 2                      

# Wykres

fig, [ax1, ax2] = plt.subplots (nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, X_mag_plot, '.-')
ax1.set_xlabel('Czas w s')
ax2.set_xlabel('Czestotliwosc (Hz)')
ax1.grid()
ax2.grid()

ax1.set_xlim(0, t[-1])
ax2.set_xlim(0, f_plot[-1])
plt.tight_layout()


plt.show()