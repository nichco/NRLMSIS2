import csdl_alpha as csdl
import numpy as np
from scipy.interpolate import Akima1DInterpolator
import pickle
import pkg_resources





# custom atmosphere model
class Atmosphere(csdl.CustomExplicitOperation):

    def __init__(self):
        """NRLMSIS2.0 atmosphere function implemented as a custom explicit operation."""
        super().__init__()
            
        # assign parameters to the class
        path = pkg_resources.resource_filename(__name__, 'data/akima_fit.pkl')
        file = open(path, 'rb')
        akima_fit = pickle.load(file)
        self.akima_density = akima_fit['akima_density']
        self.akima_density_derivative = akima_fit['akima_density_derivative']
        self.akima_temperature = akima_fit['akima_temperature']
        self.akima_temperature_derivative = akima_fit['akima_temperature_derivative']


    # def evaluate(self, inputs: csdl.VariableGroup):
    def evaluate(self, altitude: csdl.Variable):
        # assign method inputs to input dictionary
        self.declare_input('altitude', altitude)

        # declare output variables
        density = self.create_output('density', altitude.shape)
        temperature = self.create_output('temperature', altitude.shape)
        speed_of_sound = self.create_output('speed_of_sound', altitude.shape)

        # construct output of the model
        outputs = csdl.VariableGroup()
        outputs.density = density
        outputs.temperature = temperature
        outputs.speed_of_sound = speed_of_sound

        return outputs
    
    def compute(self, input_vals, output_vals):
        altitude = input_vals['altitude']

        output_vals['density'] = self.akima_density(altitude)
        output_vals['temperature'] = self.akima_temperature(altitude)
        output_vals['speed_of_sound'] = (1.4 * 287 * output_vals['temperature']) ** 0.5

    def compute_derivatives(self, input_vals, outputs_vals, derivatives):
        altitude = input_vals['altitude']

        derivatives['density', 'altitude'] = np.diag(self.akima_density_derivative(altitude))
        derivatives['temperature', 'altitude'] = np.diag(self.akima_temperature_derivative(altitude))
        derivatives['speed_of_sound', 'altitude'] = (1.4 * 287 / (2 * np.sqrt(1.4 * 287 * outputs_vals['temperature']))) * derivatives['temperature', 'altitude']








if __name__ == '__main__':

    recorder = csdl.Recorder(inline=True)
    recorder.start()

    altitude = csdl.Variable(value=np.ones(10) * 0)

    atm = Atmosphere()
    outputs = atm.evaluate(altitude)
    temperature = outputs.temperature
    density = outputs.density
    speed_of_sound = outputs.speed_of_sound

    recorder.stop()

    sim = csdl.experimental.PySimulator(recorder)
    sim.check_totals(ofs=[density, temperature, speed_of_sound], wrts=[altitude])
    sim.run()


    print(density.value)
    print(temperature.value)
    print(speed_of_sound.value)