# 2016 - The Big Bell test project
#
# In this file we show how to process a dataset filtering first a subgroup
# with those properties we want to study, while not taking into account
# those values we are not interested in. The motivation is to reduce the amount
# of data to be processed, relaxing therefore CPU and memory requirements.
#
# In this example we show how to keep only that information coming from female
# participants.
#
# Carlos Abellan

import pandas as pd
import numpy as np

# Set the directory where the raw panda datasets are located
path_to_pandas_files = './pandas/'
frames = []
TOTAL_FILES_TO_PROCESS = 10

for k in np.arange(1,TOTAL_FILES_TO_PROCESS+1,1):
    df = pd.read_csv(path_to_pandas_files+'data_pandas_'+str(k)+'.dat', sep='\t')
    frames.append(df[df.Gender=='fem'])

# Now, we concatenate all the individual files
dataset = pd.concat(frames)
print(dataset)
