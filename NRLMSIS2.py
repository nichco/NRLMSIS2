import pickle
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)

file = open('density.pkl', 'rb')
rho = pickle.load(file)

eps = 1E-12
alt = np.arange(0, 1000 + eps, 10)


plt.plot(alt, rho)
plt.show()
