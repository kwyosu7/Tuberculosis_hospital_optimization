#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
year = 2014
P_path = '/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/sigungu_age_population/'+str(year)+'_population_age.csv'
path_N='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_N.csv'
P_data = pd.read_csv(P_path)
N_data = pd.read_csv(path_N)
N_P = N_data.iloc[:, 2:]/P_data.iloc[:,2:]
# %%
N_P
# %%
P_data
# %%
