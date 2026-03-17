import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Hi guillotine..!!")
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
s = pd.Series(arr)
print(s)
plt.scatter(arr,arr)
plt.show()

def add(a, b):
    return a + b