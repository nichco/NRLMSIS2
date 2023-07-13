import csdl
import python_csdl_backend
import numpy as np
import pickle
from smt.surrogate_models import RBF
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)


file = open('density.pkl', 'rb')
rho_data = pickle.load(file)

eps = 1E-12
alt = np.arange(0, 1000 + eps, 10)

sm = RBF(d0=50, print_global=False, print_solver=False,)
sm.set_training_values(alt, rho_data)
sm.train()


class Atm(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        altitude = self.declare_variable('altitude', val=0)

        rho = csdl.custom(altitude, op=AtmExplicit())
        self.register_output('rho', rho)

class AtmExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        pass
    def define(self):
        self.add_input('altitude')
        self.add_output('rho')
        self.declare_derivatives('rho', 'altitude')

    def compute(self, inputs, outputs):
        outputs['rho'] = sm.predict_values(inputs['altitude'])

    def compute_derivatives(self, inputs, derivatives):
        drdh = sm.predict_derivatives(inputs['altitude'], 0)
        derivatives['rho', 'altitude'] = drdh







if __name__ == '__main__':

    z = np.arange(0, 1000 + eps, 1)
    data = np.zeros((len(z)))
    for i, h in enumerate(z):

        sim = python_csdl_backend.Simulator(Atm())
        sim['altitude'] = h
        sim.run()

        data[i] = sim['rho']

    #print(sim['rho'])


    plt.plot(alt, rho_data, color='limegreen',zorder=0)
    plt.scatter(alt, rho_data,s=40,zorder=5,color='purple',edgecolors='black',linewidth=0.5,alpha=0.5)
    plt.plot(z, data, color='purple',zorder=10)
    # plt.xlim(0,200)
    plt.show()