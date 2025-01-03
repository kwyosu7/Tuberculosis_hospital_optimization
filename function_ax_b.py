#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'Helvetica'
import sys
#%%
year=int(sys.argv[1])#2014
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
def E(data):
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

def consideration_weight_b(a, data):
    E_0 = sum(data['D'])
    t_list = [N_age, 55, 65, 75, 85]
    eta_i = data['h']/data['A']
    RNage_list_49= ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    E_a,c=0,0
    for t in ['0_49', '50_59', '60_69', '70_79', '80_']:
        if t=='0_49': N_it=N_49
        else: N_it=data['N']*data['RN'+t]
        phi_it= np.exp(-eta_i/data['eta_tilde'+t])
        # E=sumsum(at+b)(Nphi)
        E_a+=(a*t_list[c]) * N_it*phi_it 
        c+=1
    return (E_0-sum(E_a))/(E_0) # b

def E_consideratoin_weight(a, b, data, h_opt):
    t_list = [N_age, 55, 65, 75, 85]
    eta_i = h_opt['h']/data['A']
    RNage_list_49= ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    E,c=0,0
    for t in ['0_49', '50_59', '60_69', '70_79', '80_']:
        if t=='0_49': N_it=N_49
        else: N_it=data['N']*data['RN'+t]
        phi_it= np.exp(-eta_i/data['eta_tilde'+t])
        # E=sumsum(at+b)(Nphi)
        E+=(a*t_list[c]+b)*N_it*phi_it 
        c+=1
    return sum(E)


# %%
b=[]
ai=0
for a in np.linspace(0,0.013, 10):
    dh = 0.01
    h_opt = pd.DataFrame(data['h'].copy())
    # a=0.013
    b=consideration_weight_b(a, data)
    index_list = list(data.index)
    E_list=[]
    Ei = E_consideratoin_weight(a,b,data,h_opt)
    c=0
    for i in range(100000):
        E_list.append(Ei)
        Rsigungu = random.sample(index_list, 2)
        if h_opt.loc[Rsigungu[1], 'h'] <=0:pass
        else:
            h_opt.loc[Rsigungu[0], 'h'] += dh
            h_opt.loc[Rsigungu[1], 'h'] -= dh
            Ef = E_consideratoin_weight(a,b,data,h_opt)
            if Ei <= Ef:
                h_opt.loc[Rsigungu[0], 'h'] -= dh
                h_opt.loc[Rsigungu[1], 'h'] += dh
            else:
                Ei=Ef
                c+=1

    save_path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/at_b/opt_h_E/'
    E_list=np.array(E_list)
    np.save(save_path+str(year)+'_age_E_a_'+str(ai)+'.npy',E_list,allow_pickle=True)
    h_opt.to_csv(save_path+str(year)+'MC_age_h_opt_a_'+str(ai)+'.csv',index=False)
    ai+=1
# #%%
# plt.plot(E_list)
# # %%
# c
# # %%
# E_optimization()
# # %%
# E_list[-1]
# # %%
 
# plt.scatter(np.linspace(0,0.013, 10),b)
# # plt.yscale('log')
# plt.xlabel(r'$a$',size=20)
# plt.ylabel(r'$b$',size=20)
# plt.tight_layout()
# plt.show()
# #%%
# str(0.01)
# %%
