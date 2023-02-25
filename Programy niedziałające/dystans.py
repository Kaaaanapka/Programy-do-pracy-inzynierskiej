import numpy as np
import pandas as pd
import math

# Read data
data = pd.read_csv('data.csv')

# Create distance matrix
dist = np.zeros((len(data), len(data)))
for i in range(len(data)):
    for j in range(len(data)):
        dist[i,j] = math.sqrt((data.iloc[i,0] - data.iloc[j,0])**2 + (data.iloc[i,1] - data.iloc[j,1])**2)

# Save distance matrix
np.savetxt('dist.csv', dist, delimiter=',')