import pickle
import csdl_alpha as csdl
import numpy as np
from scipy.interpolate import Akima1DInterpolator
import matplotlib.pyplot as plt


file = open('density_0_1000_1.pkl', 'rb')
density = pickle.load(file)

file = open('altitude_0_1000_1.pkl', 'rb')
altitude = pickle.load(file)



xs = np.linspace(min(altitude), max(altitude), 300)
akima = Akima1DInterpolator(altitude, density, method="akima")
y_akima = akima(xs)


y_akima_der = Akima1DInterpolator.derivative(akima)(xs)


plt.plot(altitude, density, label='NRLMSIS2.0 data')
plt.plot(xs, y_akima, label='akima fit')
# plt.plot(xs, y_akima_der, label='derivative')

plt.yscale('log')
plt.xlabel('Altitude (m)')
plt.ylabel('Density (kg/m^3)')
plt.legend()
plt.grid()
plt.xlim(min(altitude), max(altitude))
plt.show()



plt.plot(xs, y_akima_der, label='derivative')
plt.show()