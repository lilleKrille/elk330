
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##OPPGÅVE 2
byer = ["Cardiff", "Bristol", "Greenwich", "Bergen", "Oslo"]
lengdegrader = [-3.2, -2.6, 0, 5.3, 10.8]

#make a dataframe
df = pd.DataFrame({"by": byer, "lengdegrad": lengdegrader})
#print the dataframe
df["tidsforskjell"] = (df["lengdegrad"]*4).round().astype(int)


##
#
# OPPGÅVE 4

load_data = pd.read_csv("elk320/elk330/ovingar/Oving4/load_data.csv")

##Endre datatyper

load_data["Time(UTC)"] = pd.to_datetime(
    load_data["Time(Local)"],
    format="%d.%m.%Y %H:%M:%S %z",
    utc=True
)
load_data["Consumption"] = (load_data["Consumption"]
    .str.replace(",", ".")
    .astype(float)
)

load_data["Production"] = (load_data["Production"]
    .str.replace(",", ".")
    .astype(float)
)

load_data.set_index("Time(UTC)", inplace=True)
#print(load_data.head())
#print(load_data.dtypes)
#print(load_data.loc["2026-02-03 03:00"])

last_dogn = load_data.loc["2026-02-03 00:00" : "2026-02-04 00:00"]
#last_dogn["Date"] = last_dogn.index.date
#print(last_dogn["Consumption"].head())
t = np.arange(0, len(last_dogn))
plt.plot(t, last_dogn["Consumption"])
plt.xlabel("Tid")
plt.ylabel("Konsum (kWh)")
plt.title("Forbruk dato: " + str(last_dogn.index.date[0]))

#save image
plt.savefig("elk320/elk330/ovingar/Oving4/forbruk_dato.png")

#Oppgåve 7
load_data["netto"] =(
    load_data["Production"]
    - load_data["Consumption"]
)
max_last = load_data["Consumption"].max().round(2)
min_last = load_data["Consumption"].min().round(2)
snitt_last = load_data["Consumption"].mean().round(2)
#print("max_last: ", max_last)
#print("min_last: ", min_last)
#print("snitt_last: ", snitt_last)

max_netto_punkt = load_data.loc[load_data["netto"] == load_data["netto"].max()]
min_netto_punkt = load_data.loc[load_data["netto"] == load_data["netto"].min()]
#print("max_netto: ", max_netto_punkt["netto"].round(2))
#print("min_netto: ", min_netto_punkt["netto"].round(2))

totalt_produksjon = load_data["Production"].sum().round(2)
#print("totalt_produksjon: ", totalt_produksjon)

##Oppgåve 11
load_data.plot(
    y =["Consumption", "Production"],
    figsize=(10, 5)
)
plt.xlabel("Tid")
plt.ylabel("Konsum (kWh) / Produksjon (kWh)")
plt.title("Forbruk og produksjon")
plt.grid(True)
plt.show()

load_data.plot(
    y = ["Consumption", "Production", "netto"],
    figsize=(10, 5)
)
plt.xlabel("Tid")
plt.ylabel("Konsum (kWh) / Produksjon (kWh) / Netto (kWh)")
plt.title("Forbruk og produksjon")
plt.grid(True)
plt.show()
