import numpy as np                          ## deklarowanie bibliotek
import matplotlib.pyplot as plt             ## deklarowanie bibliotek

A = 7                ##amplituda amplitude
f = 2                  #czestotliwosc frequency
phi = 0                    ##faza Phase
sr = 100                   ## sampling rate       

time = np.arange(0, 10, 1/sr)           ##0.01 sec
y = A* np.sin(2*np.pi*f*time + phi)       ##wzór

plt.figure(figsize=(10,4))
plt.plot(time,y)
plt.title("Wykres sinosoidalny")
plt.xlabel("Czas (s) ")
plt.ylabel("Amplituda")
plt.show()
