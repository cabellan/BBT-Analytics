# 2016 - The Big Bell test project
#
# In this file we show an example on how to process the datasets:
#   (1. ) Processing the mean values for participations in Mission 1
#   (2. ) Processing the mean values for female participations in Mission 1
#
# Carlos Abellan

import pandas as pd
import numpy as np
import pylab as plt

# Set the directory where the raw panda datasets are located
path_to_pandas_files = './pandas/'
frames = []
TOTAL_FILES_TO_PROCESS = 10

for k in np.arange(1,TOTAL_FILES_TO_PROCESS+1,1):
    df = pd.read_csv(path_to_pandas_files+'data_pandas_'+str(k)+'.dat', sep='\t')
    frames.append(df)

# Now, we concatenate all the individual files
dataset = pd.concat(frames)
print(dataset)
# ---- dataset contains all the information.

# Some examples on how to use datasets from Pandas.
# 1. How to obtain a given property for some subset?
means_for_mission_1 = dataset[dataset.Mission == 1].Mean.values
h, b = np.histogram(means_for_mission_1, 32)
plt.figure(1); plt.plot(b[0:32], h); plt.show();

# 2. Using the following syntax, we can filter by two properties (or more)
means_for_mission_1_female = dataset[(dataset.Mission == 1) & (dataset.Gender=='fem')].Mean.values
h, b = np.histogram(means_for_mission_1_female, 32)
plt.figure(2); plt.plot(b[0:32], h); plt.show();
