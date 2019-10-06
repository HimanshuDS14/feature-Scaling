import pandas as pd
import numpy as np

data = pd.read_csv("sample1.csv")
print(data)

min_of_s1 = np.min(data["s1"])
max_of_s1 = np.max(data["s1"])


x1 = np.array(data["s1"] , dtype=np.float)


for count , i in enumerate(x1):
    x1[count] = (i-min_of_s1)/(max_of_s1 - min_of_s1)

#print(x1)


print("***************After feature scaling***************************")
min_of_s2 = np.min(data["s2"])
max_of_s2 = np.max(data["s2"])

x2 = np.array(data["s2"] , dtype=np.float)

for count , i in enumerate(x2):
    x2[count] = (i-min_of_s2) /(max_of_s2 - min_of_s2)

#print(x2)

print("After scaling")

data["s1"] = x1
data["s2"] = x2
print(data.head())

