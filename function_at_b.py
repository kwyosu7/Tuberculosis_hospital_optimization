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
year=2014#int(sys.argv[1])#2014
path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/dataframe_40/'+str(year)+'_40.txt'
data = pd.read_csv(path,sep=',')
#%%
data
# %%
h_opt = pd.DataFrame(data['h'].copy())

# %%
h_opt
# %%
def E(data_, h_pd=None, a=None):
	if isinstance(h_pd, pd.DataFrame): eta = h_pd['h']/data_['A']
	else: eta = data_['h']/data_['A']
	if a==None: a=0
	E=0
	t = [45, 55, 65, 75, 85]
	age = ['40_49', '50_59', '60_69', '70_79', '80_']
	for i in range(5):
		phi_t = np.exp(-eta/data_['eta_tilde'+age[i]])
		N_t = data_['RN'+age[i]]*data_['N']
		E+=sum((a*t[i]+b(data_,a))*N_t*phi_t)
	return E

def b(data_, a):
	atNp, E_0 = 0,0
	eta = data_['h']/data_['A']
	t = [45, 55, 65, 75, 85]
	age = ['40_49', '50_59', '60_69', '70_79', '80_']
	for i in range(5): 
		E_0 += sum(data_['RD'+age[i]]*data_['D'])
		phi_t = np.exp(-eta/data_['eta_tilde'+age[i]])
		N_t = data_['RN'+age[i]]*data_['N']
		atNp += sum( a*t[i]*N_t*phi_t)
	return (E_0-atNp)/E_0 # b


# %%
E_0=0
age = ['40_49', '50_59', '60_69', '70_79', '80_']
for i in range(5): 
	E_0+=sum(data['RD'+age[i]]*data['D'])
E_0
# %%
a=np.linspace(0,0.013,10)
b_list=[]
for i in a: b_list.append(b(data,i))
plt.plot(a, b_list)
plt.show()
# %%
b_list[9]
# %%
"""
CHECK a=0 & a=0.003
"""
a_=0.003
dh = 0.01
h_opt = pd.DataFrame(data['h'].copy())
# b=consideration_weight_b(a, data)
index_list = list(data.index)
E_list=[]
Ei = E(data,h_pd=h_opt,a=a_)
c=0
for i in range(1000):
	E_list.append(Ei)
	Rsigungu = random.sample(index_list, 2)
	if h_opt.loc[Rsigungu[1], 'h'] <=0:pass
	else:
		h_opt.loc[Rsigungu[0], 'h'] += dh
		h_opt.loc[Rsigungu[1], 'h'] -= dh
		Ef = E(data,h_pd=h_opt,a=a_)
		if Ei <= Ef:
			h_opt.loc[Rsigungu[0], 'h'] -= dh
			h_opt.loc[Rsigungu[1], 'h'] += dh
		else:
			Ei=Ef
			c+=1

# %%
E_list
# %%
E(data, a=0.003)
# %%
b(data,a=0)
# %%
