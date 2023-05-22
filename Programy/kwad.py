import sounddevice as sd
import numpy as np

from scipy import signal

import matplotlib.pyplot as plt


Fs = 16000

t = np.linspace(0, 3, Fs, endpoint=False)
x = signal.square(2 * np.pi * 1 * t)

sd.play(x, Fs)
plt.plot(t, x)


plt.xlabel("Czas(s)")
plt.ylabel("Dźwięk")
plt.show()