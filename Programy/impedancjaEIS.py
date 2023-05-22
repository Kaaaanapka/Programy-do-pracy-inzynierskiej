import numpy as np
import matplotlib.pyplot as plt

# Parametry obwodu RC
R = 10  # Rezystancja [Ohm]
C = 1e-6  # Pojemność [Farad]

# Tworzenie częstotliwości
frequencies = np.logspace(-1, 5, num=50)  # Przykładowe częstotliwości (uwzględniające 0 Hz)

# Obliczanie impedancji teoretycznej dla obwodu RC
Z_theoretical_RC = R / (1 + 1j * 2 * np.pi * frequencies * R * C)

# Obliczanie impedancji teoretycznej dla obwodu R-RC
Z_theoretical_RRC = (R / 2) / (1 + 1j * 2 * np.pi * frequencies * R * C)

# Obliczanie impedancji teoretycznej dla obwodu RC-RC
Z_theoretical_RCRC = (2 * R) / (1 + 1j * 2 * np.pi * frequencies * R * C)  # Przykładowa konfiguracja

# Generowanie sztucznych danych pomiarowych 
Z_measured_RC = Z_theoretical_RC + np.random.normal(scale=0.1, size=Z_theoretical_RC.shape)
Z_measured_RRC = Z_theoretical_RRC + np.random.normal(scale=0.1, size=Z_theoretical_RRC.shape)
Z_measured_RCRC = Z_theoretical_RCRC + np.random.normal(scale=0.1, size=Z_theoretical_RCRC.shape)

# Wyświetlanie wyników
print("Parametry obwodu RC:")
print("R =", R)
print("C =", C)

# Wykres Nyquista
plt.figure()
plt.plot(Z_measured_RC.real, -Z_measured_RC.imag, "o", label="Pomiar RC")
plt.plot(Z_measured_RRC.real, -Z_measured_RRC.imag, "o", label="Pomiar R-RC")
plt.plot(Z_measured_RCRC.real, -Z_measured_RCRC.imag, "o", label="Pomiar RC-RC")
plt.plot(Z_theoretical_RC.real, -Z_theoretical_RC.imag, label="Teoria RC")
plt.plot(Z_theoretical_RRC.real, -Z_theoretical_RRC.imag, label="Teoria R-RC")
plt.plot(Z_theoretical_RCRC.real, -Z_theoretical_RCRC.imag, label="Teoria RC-RC")
plt.xlabel("Re(Z)")
plt.ylabel("-Im(Z)")
plt.legend()
plt.show()
