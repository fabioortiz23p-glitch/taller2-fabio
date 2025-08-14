import numpy as np
import pandas as pd
df = pd.read_csv("BikePrices.csv")
df

def owner_label(x):
  if x=="1st owner":
    return 1
  elif x=="2nd owner":
    return 2
  elif x=="3rd owner":
    return 3
  else:
    return 4
  
owner_new = df["Owner"].map(owner_label)
print(owner_new)