import pickle
import csdl_alpha as csdl
import numpy as np
from scipy.interpolate import Akima1DInterpolator
import matplotlib.pyplot as plt


file = open('NRLMSIS2/data/density_0_1000_1.pkl', 'rb')
density = pickle.load(file)

file = open('NRLMSIS2/data/altitude_0_1000_1.pkl', 'rb')
altitude = pickle.load(file)

file = open('NRLMSIS2/data/temperature_0_1000_1.pkl', 'rb')
temperature = pickle.load(file)

akima_density = Akima1DInterpolator(altitude, density, method="akima")
akima_density_derivative = Akima1DInterpolator.derivative(akima_density)

akima_temperature = Akima1DInterpolator(altitude, temperature, method="akima")
akima_temperature_derivative = Akima1DInterpolator.derivative(akima_temperature)


dict = {'akima_density': akima_density, 
        'akima_density_derivative': akima_density_derivative, 
        'akima_temperature': akima_temperature, 
        'akima_temperature_derivative': akima_temperature_derivative}

with open('akima_fit.pkl', 'wb') as f:
    pickle.dump(dict, f)



# exit()
# xs = np.linspace(min(altitude), max(altitude), 300)
# akima = Akima1DInterpolator(altitude, density, method="akima")
# y_akima = akima(xs)


# y_akima_der = Akima1DInterpolator.derivative(akima)(xs)


# plt.plot(altitude, density, label='NRLMSIS2.0 data')
# plt.plot(xs, y_akima, label='akima fit')
# # plt.plot(xs, y_akima_der, label='derivative')

# plt.yscale('log')
# plt.xlabel('Altitude (m)')
# plt.ylabel('Density (kg/m^3)')
# plt.legend()
# plt.grid()
# plt.xlim(min(altitude), max(altitude))
# plt.show()



# plt.plot(xs, y_akima_der, label='derivative')
# plt.show()