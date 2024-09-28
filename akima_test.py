import pickle
import csdl_alpha as csdl
import numpy as np
from scipy.interpolate import Akima1DInterpolator
import matplotlib.pyplot as plt


file = open('density_0_149_1.pkl', 'rb')
density = pickle.load(file)

file = open('altitude_0_149_1.pkl', 'rb')
altitude = pickle.load(file)



xs = np.linspace(min(altitude), max(altitude), 300)
y_akima = Akima1DInterpolator(altitude, density, method="akima")(xs)
y_makima = Akima1DInterpolator(altitude, density, method="makima")(xs)



plt.plot(altitude, density, label='data')
plt.plot(xs, y_akima, label='akima')
plt.plot(xs, y_makima, label='makima')

plt.yscale('log')
plt.xlabel('Altitude (m)')
plt.ylabel('Density (kg/m^3)')
plt.legend()
plt.grid()
plt.show()
