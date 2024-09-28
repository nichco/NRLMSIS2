import numpy as np




def std_atm(alt):
        R = 287 # J/kg-K

        if alt > 25000:
            T = -131.21 + 0.00299 * alt
            density = (2.488 * (((T + 273.1) / 216.6) ** -11.388)) / (0.2869 * (T + 273.1))
        elif 11000 < alt <= 25000:
            T = -56.46
            density = (22.65 * np.exp(1.73 - 0.000157 * alt)) / (0.2869 * (T + 273.1))
        elif alt <= 11000:
            T = 15.04 - 0.00649 * alt
            density = (101.29 * (((T + 273.1) / 288.08) ** 5.256)) / (0.2869 * (T + 273.1))

        T = T + 273.15 # result in K 
        pressure = density * R * T / 100 # result in hPa    

        return density, pressure, T