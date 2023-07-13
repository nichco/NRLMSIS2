import csdl
import python_csdl_backend
import numpy as np
import pickle
from smt.surrogate_models import RBF, RMTB, KRG
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)


file = open('density.pkl', 'rb')
rho_data = pickle.load(file)

eps = 1E-12
alt = np.arange(0, 1000 + eps, 10)

coefs = np.polyfit(alt, rho_data, 12)


class Atm(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        h = self.declare_variable('altitude', val=0)

        #px = p[0]*x**(N-1) + p[1]*x**(N-2) + p[2]*x**(N-3) + p[3]*x**(N-4) + p[4]*x**(N-5)...
        temp = self.create_output('temp', shape=(len(coefs)), val=0)
        for i in range(len(coefs)):
            temp[i] = coefs[i]*h**(len(coefs) - 1 - i)

        rho = csdl.sum(temp)
        self.register_output('rho', rho)



if __name__ == '__main__':

    data = np.zeros((len(alt)))
    for i, h in enumerate(alt):

        sim = python_csdl_backend.Simulator(Atm())
        sim['altitude'] = h
        sim.run()

        data[i] = sim['rho']

    #print(sim['rho'])


    plt.plot(alt, rho_data)
    plt.plot(alt, data)
    plt.show()