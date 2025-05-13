import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import sys

"""
Input
"""

"""
DEF FUNCTION
"""
def E(data_, h_pd=None, a=None, b=None):
	if isinstance(h_pd, pd.DataFrame): eta = h_pd['h']/data_['A']
	else: eta = data_['h']/data_['A']
	if a==None: a,b=0,1
	E=0
	t = [1,2,3,4,5]
	age = ['40_49', '50_59', '60_69', '70_79', '80_']
	for i in range(5):
		phi_t = np.exp(-eta/data_['eta_tilde'+age[i]])
		N_t = data_['RN'+age[i]]*data_['N']
		E+=sum((a*t[i]+b)*N_t*phi_t)
	return E

def b(data_, a):
	atNp, E_0 = 0,0
	eta = data_['h']/data_['A']
	t = [1,2,3,4,5]
	age = ['40_49', '50_59', '60_69', '70_79', '80_']
	for i in range(5): 
		E_0 += sum(data_['RD'+age[i]]*data_['D'])
		phi_t = np.exp(-eta/data_['eta_tilde'+age[i]])
		N_t = data_['RN'+age[i]]*data_['N']
		atNp += sum( a*t[i]*N_t*phi_t)
	return (E_0-atNp)/E_0 # b

"""
Main
"""

ai = int(sys.argv[1])# 0~30, 31개
a = np.linspace(-2, 1, 31)[ai]
dh = 0.01
for year in range(2014,2023):
    path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/data_over40/'+str(year)+'_40.txt'
    data = pd.read_csv(path,sep=',')
    h_opt = pd.DataFrame(data['h'].copy())
    index_list = list(data.index)
    E_list=[]
    b_=b(data, a)
    Ei = E(data,h_pd=h_opt,a=a,b=b_)
    c=0
    for i in range(100000):
        E_list.append(Ei)
        Rsigungu = random.sample(index_list, 2)
        if h_opt.loc[Rsigungu[1], 'h'] - dh <0:pass
        else:
            h_opt.loc[Rsigungu[0], 'h'] += dh
            h_opt.loc[Rsigungu[1], 'h'] -= dh
            Ef = E(data,h_pd=h_opt,a=a,b=b_)
            if Ei <= Ef:
                h_opt.loc[Rsigungu[0], 'h'] -= dh
                h_opt.loc[Rsigungu[1], 'h'] += dh
            else:
                Ei=Ef
                c+=1

    save_path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/at_b_tau12345/opt_E_h_a2_1/'
    E_list=np.array(E_list)
    np.save(save_path+str(year)+'_age_E_a_'+str(ai)+'.npy',E_list,allow_pickle=True)
    h_opt.to_csv(save_path+str(year)+'MC_age_h_opt_a_'+str(ai)+'.csv', index=False)
    