import pandas as pd

byer = ["Cardiff", "Bristol", "Greenwich", "Bergen", "Oslo"]
lengdegrader = [-3.2, -2.6, 0, 5.3, 10.8]

#make a dataframe
df = pd.DataFrame({"by": byer, "lengdegrad": lengdegrader})
#print the dataframe
df["tidsforskjell"] = (df["lengdegrad"]*4).round().astype(int)

print(df)
