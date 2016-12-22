# 2016 - The Big Bell test project
#
# In this file we show how you can add your own metrics to the dataset for
# posterior analysis and comparisons. The idea is that you can take the raw
# bits introduced in each mission and (1) extract information you think might be
# relevant and (2) add it to the dataset so that we can process it later on.
#
# In this script we illustrate how to add a new metric to a dataset. In
# particular, we will add the correlation at 1 bit delay. The process will be
#   (1) opening each of the raw files,
#   (2) computing the new metric for each entry,
#   (3) Appending the new metric to the dataset
#   (4) Recording the new datafile to a new (or the same) directory
#
# Carlos Abellan

import pandas as pd
import numpy as np
import os

# Let's define here the new calculation we want to do. In this case, the
# correlation at 1 bit delay = 1/n \sum_i=0^{n-1} x_i * x_{i+1} - mu_x^2,
# being n the length of the array
def first_xcorr_coefficient(x):
    n = np.size(x)
    mu = np.mean(x)
    return(np.sum(x[0:n-1]*x[1:n]/n) - mu**2)

# The bits are recorded as a string, so we need a function to convert them into
# a numpy array. The following function converts the bits to a numpy array of
# -1 and 1. Namely, the mean value will be expected at 0.
def bits_string_to_array(s):
    rnd = []; fin = True; i = 0
    while fin:
        try:
            rnd.append(2*np.int(s[i])-1)
            i = i+1
        except Exception:
            fin = False
    return(np.array(rnd))

# Set the directory where the raw panda datasets are located and the path to
# the new location for the files
path_to_pandas_files = './pandasnew/'

# Set the same as in path_to_pandas_files if you want to overwrite the files or
# simply add a new name and a new directory will be created.
path_to_new_pandas_files = './pandasnew/'
if not os.path.exists(path_to_new_pandas_files):
    os.makedirs(path_to_new_pandas_files)


df = pd.read_csv(path_to_pandas_files+'data_pandas.dat', sep='\t')

# Compute the number of rows of the dataset
dataset_size = len(df.index)

# We define the new array that will store the new metric (in this case the
# correlation at distance 1)
xcorr = np.zeros(dataset_size)

# For every row, we will obtain the raw bits, and compute the correlation
for i in range(dataset_size):
    if np.mod(i, 10000) == 0:
        print( "Iteration "+str(i)+'/'+str(dataset_size) )
    aux = df.iloc[[i]].Bits.values[0]
    aux = bits_string_to_array(aux)
    xcorr[i] = first_xcorr_coefficient(aux)

# Now, create the new column and set the name: df['new_metric_name']
df['xcorr1'] = pd.Series(xcorr, index=df.index)
df.to_csv(path_to_new_pandas_files+'data_pandas.dat', sep='\t')
