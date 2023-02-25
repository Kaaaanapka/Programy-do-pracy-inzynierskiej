import sounddevice as sd
import numpy as np 
from math import pi
import matplotlib.pyplot as plot

# próbkowanie

Fs = 16000

n = np.arange(0,3,1/Fs) # przedzialy czasu
f = 100;
x = np.sin(2*pi*f*n)

#odtwarzanie dzwieku

sd.play(x, Fs)
plot.plot(n,x)
