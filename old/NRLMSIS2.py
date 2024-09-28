import pickle
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)

file = open('density.pkl', 'rb')
rho = pickle.load(file) * 100**3 / 1000

temperature = pickle.load(open('temperature.pkl', 'rb'))

eps = 1E-12
alt = np.arange(0, 1000 + eps, 10)


from std_atm import std_atm
density = np.zeros_like(alt)
temp_std = np.zeros_like(alt)
for i, h in enumerate(alt):
    std_density, _, t = std_atm(h*1E3)
    density[i] = std_density
    temp_std[i] = t


plt.plot(alt, rho)
plt.plot(alt, density)
plt.yscale('log')
plt.show()



plt.plot(alt, temperature)
plt.plot(alt, temp_std)
plt.show()