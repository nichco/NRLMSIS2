import pandas as pd
import pickle


# Read the Excel file
df = pd.read_excel('0_149.xlsx')

altitude = pd.to_numeric(df.iloc[1:, 5]).to_numpy() # km
temperature = pd.to_numeric(df.iloc[1:, 12]).to_numpy() # K
density = pd.to_numeric(df.iloc[1:, 11]).to_numpy() # g / cm^3


print('altitude: ', altitude)
print('temperature: ', temperature)
print('density: ', density)


with open('altitude_0_149_1.pkl', 'wb') as f:
    pickle.dump(altitude, f)

with open('temperature_0_149_1.pkl', 'wb') as f:
    pickle.dump(temperature, f)

with open('density_0_149_1.pkl', 'wb') as f:
    pickle.dump(density, f)