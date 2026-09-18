from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

##Gauss-curve (t,a,mu,sigma):
#
# a: amplitude
# mu: time of peak
# sigma: standard deviation

def gauss_curve(t, a, mu, sigma): return a * np.exp(-(t - mu)**2 / (2 * sigma**2))

# Modelling with gauss-curve
l_0 = [0, 10, 50, 100]
a = [100, 125, 150, 200]
mu = [3, 10, 15, 20]
sigma = [1, 2, 3, 4]

# apply gauss-curve to each l_0, a, mu, sigma
# subplots for each mu, 2x2 grid, with shared x-axis, include other values in each subplot
fig, axs = plt.subplots(2, 2, sharex=True)

t = np.linspace(0, 24, 100)
for i in range(len(mu)):
    row, col = divmod(i, 2)
    ax = axs[row, col]
    for j in range(len(mu)):
        ax.plot(t, l_0[j] + gauss_curve(t, a[j], mu[i], sigma[j]))
    ax.set_title(f"mu = {mu[i]}, sigma = {sigma[i]}")
    ax.set_xlabel("t")
    ax.set_ylabel("l_0")

plt.tight_layout()
plt.savefig("elk320/elk330/ovingar/Oving5/figurer/gauss_curve.png")

##OPPGAVE 2
load_data = pd.read_csv("C:/Users/20gus/Documents/Uis/5semester/elk320/elk330/ovingar/Oving5/data/ProductionConsumption-2026.csv")

load_data["Time(UTC)"] = pd.to_datetime(
       load_data["Time(Local)"],
    format="%d.%m.%Y %H:%M:%S %z",
    utc=True
)
load_data.set_index("Time(UTC)", inplace=True)
#print(load_data.head())
#print(load_data.dtypes)
dayload = load_data.loc["2026-05-05 00:00":"2026-05-05 23:59"]
peaks, _ = find_peaks(dayload["Consumption"])
base_load = dayload["Consumption"].min()

modell_morgen =gauss_curve(t,
        dayload["Consumption"].iloc[peaks[0]]-base_load,
        dayload.iloc[peaks[0]].name.hour,
        2
)
modell_kveld =gauss_curve(t,
        dayload["Consumption"].iloc[peaks[1]]-base_load,
        dayload.iloc[peaks[1]].name.hour,
        3
)
modell_natt = gauss_curve(t,
        dayload["Consumption"].iloc[peaks[2]]-base_load,
        dayload.iloc[peaks[2]].name.hour,
        2
)
modell_samla = base_load + modell_morgen + modell_kveld + modell_natt
print(dayload["Consumption"].iloc[peaks])
#plot in a new figure
plt.figure()
plt.scatter(dayload.index.hour, dayload["Consumption"], color="black")
plt.plot(t, modell_samla, linewidth=3)
plt.plot(t, base_load + modell_morgen, linestyle="--")
plt.plot(t, base_load + modell_kveld, linestyle="--")
plt.plot(t, base_load + modell_natt, linestyle="--")
plt.legend(["Datapunkt ""Total modell", "Morgen", "Kveld", "Natt"])
plt.savefig("elk320/elk330/ovingar/Oving5/figurer/gaussmodell.png")
plt.show()
