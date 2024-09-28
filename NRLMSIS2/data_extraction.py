import pandas as pd
import pickle
import numpy as np


# Read the Excel file
df_0_149 = pd.read_excel('NRLMSIS2/data/0_149.xlsx')
df_150_299 = pd.read_excel('NRLMSIS2/data/150_299.xlsx')
df_300_449 = pd.read_excel('NRLMSIS2/data/300_449.xlsx')
df_450_599 = pd.read_excel('NRLMSIS2/data/450_599.xlsx')
df_600_749 = pd.read_excel('NRLMSIS2/data/600_749.xlsx')
df_750_899 = pd.read_excel('NRLMSIS2/data/750_899.xlsx')
df_900_1000 = pd.read_excel('NRLMSIS2/data/900_1000.xlsx')

altitude_0_149 = pd.to_numeric(df_0_149.iloc[1:, 5]).to_numpy() # km
temperature_0_149 = pd.to_numeric(df_0_149.iloc[1:, 12]).to_numpy() # K
density_0_149 = pd.to_numeric(df_0_149.iloc[1:, 11]).to_numpy() # g / cm^3

altitude_150_299 = pd.to_numeric(df_150_299.iloc[1:, 5]).to_numpy() # km
temperature_150_299 = pd.to_numeric(df_150_299.iloc[1:, 12]).to_numpy() # K
density_150_299 = pd.to_numeric(df_150_299.iloc[1:, 11]).to_numpy() # g / cm^3

altitude_300_449 = pd.to_numeric(df_300_449.iloc[1:, 5]).to_numpy() # km
temperature_300_449 = pd.to_numeric(df_300_449.iloc[1:, 12]).to_numpy() # K
density_300_449 = pd.to_numeric(df_300_449.iloc[1:, 11]).to_numpy() # g / cm^3

altitude_450_599 = pd.to_numeric(df_450_599.iloc[1:, 5]).to_numpy() # km
temperature_450_599 = pd.to_numeric(df_450_599.iloc[1:, 12]).to_numpy() # K
density_450_599 = pd.to_numeric(df_450_599.iloc[1:, 11]).to_numpy() # g / cm^3

altitude_600_749 = pd.to_numeric(df_600_749.iloc[1:, 5]).to_numpy() # km
temperature_600_749 = pd.to_numeric(df_600_749.iloc[1:, 12]).to_numpy() # K
density_600_749 = pd.to_numeric(df_600_749.iloc[1:, 11]).to_numpy() # g / cm^3

altitude_750_899 = pd.to_numeric(df_750_899.iloc[1:, 5]).to_numpy() # km
temperature_750_899 = pd.to_numeric(df_750_899.iloc[1:, 12]).to_numpy() # K
density_750_899 = pd.to_numeric(df_750_899.iloc[1:, 11]).to_numpy() # g / cm^3

altitude_900_1000 = pd.to_numeric(df_900_1000.iloc[1:, 5]).to_numpy() # km
temperature_900_1000 = pd.to_numeric(df_900_1000.iloc[1:, 12]).to_numpy() # K
density_900_1000 = pd.to_numeric(df_900_1000.iloc[1:, 11]).to_numpy() # g / cm^3



# Concatenate the data
altitude = np.concatenate((altitude_0_149, altitude_150_299, altitude_300_449, altitude_450_599, altitude_600_749, altitude_750_899, altitude_900_1000))
temperature = np.concatenate((temperature_0_149, temperature_150_299, temperature_300_449, temperature_450_599, temperature_600_749, temperature_750_899, temperature_900_1000))
density = np.concatenate((density_0_149, density_150_299, density_300_449, density_450_599, density_600_749, density_750_899, density_900_1000))


# unit conversions
altitude = altitude * 1e3 # m
density = density * 100**3 / 1000 # kg / m^3


# print('altitude: ', altitude)
# print('temperature: ', temperature)
# print('density: ', density)


# with open('altitude_0_1000_1.pkl', 'wb') as f:
#     pickle.dump(altitude, f)

# with open('temperature_0_1000_1.pkl', 'wb') as f:
#     pickle.dump(temperature, f)

# with open('density_0_1000_1.pkl', 'wb') as f:
#     pickle.dump(density, f)