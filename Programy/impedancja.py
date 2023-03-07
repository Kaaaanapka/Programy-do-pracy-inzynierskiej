from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
import matplotlib.pyplot as plt
from impedance.visualization import plot_nyquist

#wczytywanie danych z przykładu danych EIS

freq, Z = preprocessing.readCSV('exampleData.csv')

# zachowanie danych impedancji w pierwszym kwadrancie
freq, Z = preprocessing.ignoreBelowX(freq, Z)

obwod = 'R0-p(R1,C1)-p(R2-Wo1, C2)'
initial_guess = [.01, .01, 100, .01, .05, 100, 1]

obwod = CustomCircuit(obwod, initial_guess=initial_guess)
obwod.fit(freq, Z)

print(obwod)

Z_fit = obwod.predict(freq)

fig, ax = plt.subplots()
plot_nyquist (Z, fmt='o', scale=10, ax=ax)
plot_nyquist (Z_fit, fmt='-', scale=10, ax=ax)

plt.legend(['Dane', 'Fit'])
plt.show()