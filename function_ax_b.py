#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'Helvetica'
#%%
year=2014
path_N='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_N.csv'
path_D='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_D.csv'
path='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/DSL_data/'+str(year)+'.txt'
data_age_N = pd.read_csv(path_N)
data_age_D = pd.read_csv(path_D)
data = pd.read_csv(path,sep='\t')
#%%
age_list_49= ['0_9', '10_19', '20_29', '30_39', '40_49']
Total_N_49=np.sum(data_age_N[age_list_49].sum(axis=1))
N_age=0
for a in age_list_49:
    N_age += np.sum(data_age_N[a])/Total_N_49*(int(a[0])*10+5)
N_age # the average age of 0~49 age

#%%
Total_N_49

# %%
def E():
    eta_i = data['h']/data['A']
    RNage_list_49= ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    E=0
    for t in ['0_49', '50_59', '60_69', '70_79', '80_']:
        if t=='0_49': N_it=N_49
        else: N_it=data['N']*data['RN'+t]
        phi_it= np.exp(-eta_i/data['eta_tilde'+t])
        E+=N_it*phi_it
    return sum(E)

def E_optimization():
    eta_i = data['eta_age_simul']
    RNage_list_49= ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    E=0
    for t in ['0_49', '50_59', '60_69', '70_79', '80_']:
        if t=='0_49': N_it=N_49
        else: N_it=data['N']*data['RN'+t]
        phi_it= np.exp(-eta_i/data['eta_tilde'+t])
        E+=N_it*phi_it
    return sum(E)

def E_consideratoin_weight(a):
    E_0 = sum(data['D'])
    a_list = [N_age, 55, 65, 75, 85]
    

    eta_i = data['h']/data['A']
    RNage_list_49= ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    E,c=0,0
    for t in ['0_49', '50_59', '60_69', '70_79', '80_']:
        if t=='0_49': N_it=N_49
        else: N_it=data['N']*data['RN'+t]
        phi_it= np.exp(-eta_i/data['eta_tilde'+t])
        E+=N_it*phi_it
        
        c+=1
    b = (E_0-)/5

    return sum(E)
# %%
N_age
# %%
