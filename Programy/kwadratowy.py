import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd


x = np.linspace(0, 3, 300)
y = np.zeros(300)
start = 0
Ton = 50
stop = Ton
amp = 14000               #amplituda
state = 0 

for i in range (start,stop):
    y[i] = amp
    if stop == Ton:
        while state<1:
            state += 1 
            start += 10
            stop += 10
            for j in range (start, stop):
                y[j] = amp
        while state<2:
            state += 1 
            start += 150
            stop += 150
            for j in range (start, stop):
                y[j] = amp


plt.plot(x, y)
plt.xlabel("Czas(s)")
plt.ylabel("Dźwięk")
plt.show()