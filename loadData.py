

import pandas as pd
import numpy as np

loadData = pd.read_csv('elk320/elk330/load_data.csv')
loadData["Time(UTC)"] = pd.to_datetime(
    loadData["Time(Local)"],
    format="%d.%m.%Y %H:%M:%S %z",
    utc=True)
loadData = loadData.set_index("Time(UTC)")

loadData["Consumption"] = loadData["Consumption"].str.replace(",", ".").astype(float)

loadData["date"] = loadData.index.date
loadData["year"] = loadData.index.year

analyse_måned = loadData['Consumption'].resample("ME").mean()

daglig = loadData.groupby("date")["Consumption"].apply(list)

daglig = daglig[daglig.apply(len) == 24]

X = np.vstack(daglig.values)

snittprofil = X.mean(axis=0)
avstander = np.linalg.norm(X - snittprofil, axis=1)

repDag = np.argmin(avstander)
rep_profil = X[repDag]
rep_dato = daglig.index[repDag]

print(rep_dato)
