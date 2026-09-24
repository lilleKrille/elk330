from matplotlib.cm import tab10
import pandas as pd
from scipy.signal import find_peaks
from elk320.funksjoner import gauss_curve #Eiga funksjoner-fil
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 100)
A = 800
mu = 12
sigma = 2.5
g = gauss_curve(t, A, mu, sigma)

plt.plot(t, g)
plt.xlabel('Tid (t)')
plt.ylabel('G(t)')
plt.title('Gauss-kurve for solstråling G(t)')
plt.savefig('elk320/elk330/ovingar/Oving6/gauss_curve_sol.png')

#Del 2

df = pd.read_csv('elk320/elk330/ovingar/Oving6/data/Timeseries_59.735_6.756_SA3_36deg_0deg_2018_2018.csv', skiprows = 8, skipfooter=9)
df["time"] = pd.to_datetime(df["time"], format="%Y%m%d:%H%M", utc=True)
solDag = df[df["time"].dt.dayofyear == 182]

#new figure
#
plt.figure()
t_dag = np.linspace(0, 23, len(solDag))
print(df.dtypes)
plt.plot(t_dag, solDag["G(i)"])
plt.plot(t, gauss_curve(t, solDag["G(i)"].max(), find_peaks(solDag["G(i)"])[0][0], 3))

plt.xlabel('Tid (t)')
plt.ylabel('G(i)')
plt.title('Solstråling G(i)')
plt.savefig('elk320/elk330/ovingar/Oving6/solstråling.png')
#print all paramaters
print(f"Max: {solDag['G(i)'].max()}, Peak: {find_peaks(solDag['G(i)'])[0][0]}, Std: {solDag['G(i)'].std()}")
