import csdl_alpha as csdl
import numpy as np
from scipy.interpolate import Akima1DInterpolator
import pickle





# custom atmosphere model
class Atmosphere(csdl.CustomExplicitOperation):

    def __init__(self):
        """NRLMSIS2.0 atmosphere function implemented as a custom explicit operation."""
        super().__init__()
            
        # assign parameters to the class
        file = open('altitude_0_1000_1.pkl', 'rb')
        altitude = pickle.load(file)

        file = open('density_0_1000_1.pkl', 'rb')
        density = pickle.load(file)
        self.akima_density = Akima1DInterpolator(altitude, density, method="akima")
        self.akima_density_derivative = Akima1DInterpolator.derivative(self.akima_density)

        file = open('temperature_0_1000_1.pkl', 'rb')
        temperature = pickle.load(file)
        self.akima_temperature = Akima1DInterpolator(altitude, temperature, method="akima")
        self.akima_temperature_derivative = Akima1DInterpolator.derivative(self.akima_temperature)


    # def evaluate(self, inputs: csdl.VariableGroup):
    def evaluate(self, altitude: csdl.Variable):
        # assign method inputs to input dictionary
        self.declare_input('altitude', altitude)

        # declare output variables
        density = self.create_output('density', altitude.shape)
        temperature = self.create_output('temperature', altitude.shape)

        # construct output of the model
        outputs = csdl.VariableGroup()
        outputs.density = density
        outputs.temperature = temperature

        return outputs
    
    def compute(self, input_vals, output_vals):
        altitude = input_vals['altitude']

        output_vals['density'] = self.akima_density(altitude)
        output_vals['temperature'] = self.akima_temperature(altitude)

    def compute_derivatives(self, input_vals, outputs_vals, derivatives):
        altitude = input_vals['altitude']

        derivatives['density', 'altitude'] = self.akima_density_derivative(altitude)
        derivatives['temperature', 'altitude'] = self.akima_temperature_derivative(altitude)








if __name__ == '__main__':

    recorder = csdl.Recorder(inline=True)
    recorder.start()

    altitude = csdl.Variable(value=500000)

    atm = Atmosphere()
    outputs = atm.evaluate(altitude)
    temperature = outputs.temperature
    density = outputs.density
    speed_of_sound = (1.4 * 287 * temperature) ** 0.5

    recorder.stop()

    print(density.value)
    print(temperature.value)
    print(speed_of_sound.value)