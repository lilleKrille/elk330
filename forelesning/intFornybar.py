import pandas as pd
import requests
from pyjstat import pyjstat
import matplotlib.pyplot as plt

meta = requests.get(f"https://data.ssb.no/api/v0/no/table/08307").json()

print("Tittel:")
print(meta["title"])

TABLE = "08307"
VARIABLES = ["VindKraft", "Solkraft"]

query = {
    "query": [{
        "code": "ContentsCode",
        "selection": {
            "filter": "item",
            "values": VARIABLES
        }
    }],
    "response": {"format": "json-stat2"}
}

url = f"https://data.ssb.no/api/v0/en/table/{TABLE}"

df = pyjstat.Dataset.read(
    requests.post(url, json=query).text
).write("dataframe")

df_wide = df.pivot(
    index="year",
    columns="contents",
    values="value"
)

df_wide = df_wide.rename(columns={
    "Wind power production": "Vind",
    "Solar power production": "Sol"
})
#plot data
df_wide.plot()
plt.show()
