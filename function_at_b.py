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

# %%
def E(data_, h_pd=None, a=None, b=None):
	if isinstance(h_pd, pd.DataFrame): eta = h_pd['h']/data_['A']
	else: eta = data_['h']/data_['A']
	if a==None: a,b=0,1
	E=0
	t = [45, 55, 65, 75, 85]
	age = ['40_49', '50_59', '60_69', '70_79', '80_']
	for i in range(5):
		phi_t = np.exp(-eta/data_['eta_tilde'+age[i]])
		N_t = data_['RN'+age[i]]*data_['N']
		E+=sum((a*t[i]+b)*N_t*phi_t)
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
a_=0.013
dh = 0.01
h_opt = pd.DataFrame(data['h'].copy())
# b=consideration_weight_b(a, data)
index_list = list(data.index)
E_list=[]
b_=b(data, a_)
Ei = E(data,h_pd=h_opt,a=a_,b=b_)
c=0
for i in range(100000):
	E_list.append(Ei)
	Rsigungu = random.sample(index_list, 2)
	if h_opt.loc[Rsigungu[1], 'h'] <=0:pass
	else:
		h_opt.loc[Rsigungu[0], 'h'] += dh
		h_opt.loc[Rsigungu[1], 'h'] -= dh
		Ef = E(data,h_pd=h_opt,a=a_,b=b_)
		if Ei <= Ef:
			h_opt.loc[Rsigungu[0], 'h'] -= dh
			h_opt.loc[Rsigungu[1], 'h'] += dh
		else:
			Ei=Ef
			c+=1

# %%
E_list[-1]
# %%
plt.plot(range(100000), E_list)
# %%
h_opt
# %%
data['h']
# %%
"""
a=0
"""
a_=0.02
dh = 0.01
h_opt_0 = pd.DataFrame(data['h'].copy())
# b=consideration_weight_b(a, data)
index_list = list(data.index)
E_list_0=[]
b_=b(data, a_)
Ei = E(data,h_pd=h_opt_0,a=a_,b=b_)
c=0
for i in range(100000):
	E_list_0.append(Ei)
	Rsigungu = random.sample(index_list, 2)
	if h_opt_0.loc[Rsigungu[1], 'h'] <=0:pass
	else:
		h_opt_0.loc[Rsigungu[0], 'h'] += dh
		h_opt_0.loc[Rsigungu[1], 'h'] -= dh
		Ef = E(data,h_pd=h_opt_0,a=a_,b=b_)
		if Ei <= Ef:
			h_opt_0.loc[Rsigungu[0], 'h'] -= dh
			h_opt_0.loc[Rsigungu[1], 'h'] += dh
		else:
			Ei=Ef
			c+=1
# %%
b_=b(data, a_)
# %%
data
# %%
plt.plot(range(100000), E_list_0)
# %%
E_list_0[-1]
# %%
E_list[-1]
# %%
a=0.03
b_=b(data, a)
# %%
b_
# %%
45*a+b_
#%%
year
#%%
"""
CHECK WHOLE data
"""
save_path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/at_b/opt_E_h_a01_005/'
fig = plt.figure(figsize=(15, 9))
gs = GridSpec(3, 3, figure=fig)
c=0
for year in range(2014,2023):
	path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/dataframe_40/'+str(year)+'_40.txt'
	data = pd.read_csv(path,sep=',')
	ai=0
	E_list=[]
	for i in range(21):
		E_ = np.load(save_path+str(year)+'_age_E_a_'+str(ai)+'.npy')
		E_list.append(E_[-1])
		# h_opt = pd.read_csv(save_path+str(year)+'MC_age_h_opt_a_'+str(ai)+'.csv')
		# E_list.append(E(data, h_pd=h_opt))

		ai+=1
	ax = fig.add_subplot(gs[c//3, c%3])
	ax.scatter(np.linspace(-0.15,0.05,21), E_list, label=str(year))
	ax.set_xlabel(r'$a$',size=20)
	ax.set_ylabel(r'$E^\mathrm{opt}$',size=20)
	ax.legend()
	c+=1
plt.tight_layout()
plt.savefig('/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/figure/E_a.pdf',format='pdf',transparent=True)
plt.show()
# %%
plt.plot(range(50000), E)
# %%
a=0.03
b_ = b(data, a)
a*45+b_
# %%
a=-0.01
b_ = b(data, a)
# %%
b_
# %%
