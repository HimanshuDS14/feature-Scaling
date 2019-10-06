import numpy as np
import pandas as pd

data = pd.read_csv("sample1.csv")
print(data)

mean_of_s1 = np.mean(data["s1"])
#print(mean_of_s1)

standard_deviation_of_s1 = np.std(data["s1"])
#print(standard_deviation_of_s1)

arr = np.array(data["s1"] , dtype=np.float)

for count , i in enumerate(arr):
    arr[count] = (i-mean_of_s1)/standard_deviation_of_s1
#print(arr)


print("*********************After feature scaling******************************")

mean_of_s2 = np.mean(data["s2"])
standard_deviation_of_s2 = np.std(data["s2"])

#print(mean_of_s2)
#print(standard_deviation_of_s2)


arr2 = np.array(data["s2"] , dtype = np.float)

for count , i in enumerate(arr2):
    arr2[count]  = (i-mean_of_s2)/standard_deviation_of_s2

#print(arr2)

data["s1"] = arr
data["s2"] = arr2

print(data.head())






