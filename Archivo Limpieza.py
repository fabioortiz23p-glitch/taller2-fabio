import numpy as np
import pandas as pd
df = pd.read_csv("BikePrices.csv")
df

def owner_label(x):
  if x=="1st owner":
    return 1
  elif x=="2nd owner":
    return 3
  elif x=="3rd owner":
    return 4
  else:
    return 5
  
owner_new = df["Owner"].map(owner_label)
print("El número de dueños es: ")
print(owner_new)