#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import sys
#%%

"""
DEF FUNCTION
"""

def E(data_, h_pd, etatilde):
	eta = h_pd['h']/data_['A']
	phi_DN = data_['D']/data_['N']
	#eta_tilde = eta/np.abs(np.log(phi_DN))
	phi = np.exp(-eta/etatilde)
	E = data_['N']*phi
	return sum(E)
#%%
"""
Main
"""

year = int(sys.argv[1])# 2014~2022

dh = 0.01

path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/data_over40/'+str(year)+'_40.txt'
data = pd.read_csv(path,sep=',')
h_opt = pd.DataFrame(data['h'].copy())
etatilde = (data['h']/data['A'])/(np.abs(np.log(data['D']/data['N'])))
index_list = list(data.index)
E_list=[]
Ei = E(data,h_pd=h_opt,etatilde=etatilde)
c=0
for i in range(100000): #100000
	E_list.append(Ei)
	Rsigungu = random.sample(index_list, 2)
	if h_opt.loc[Rsigungu[1], 'h'] - dh <0:pass
	else:
		h_opt.loc[Rsigungu[0], 'h'] += dh
		h_opt.loc[Rsigungu[1], 'h'] -= dh
		Ef = E(data,h_pd=h_opt,etatilde=etatilde)
		if Ei <= Ef:
			h_opt.loc[Rsigungu[0], 'h'] -= dh
			h_opt.loc[Rsigungu[1], 'h'] += dh
		else:
			Ei=Ef
			c+=1

#%%
save_path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/no_age/opt_E_h/'
E_list=np.array(E_list)
np.save(save_path+str(year)+'_noage_E.npy',E_list,allow_pickle=True)
h_opt.to_csv(save_path+str(year)+'MC_noage_h_opt.csv', index=False)
