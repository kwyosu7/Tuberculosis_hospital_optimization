#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'Helvetica'
import sys
from matplotlib.gridspec import GridSpec
#%%
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

def z(data_, h_opt_,  a=0, b=1):
	t = [45, 55, 65, 75, 85]
	age = ['40_49', '50_59', '60_69', '70_79', '80_']
	
	for i in range(5):
		if i== 0:
			rho_t = data['RN'+age[i]] * data['N'] / data['A']
			z = (a*t[i]+b) * (rho_t/data['eta_tilde'+age[i]]) * np.exp(-h_opt['h']/data['eta_tilde'+age[i]])
		else:
			rho_t = data['RN'+age[i]] * data['N'] / data['A']
			z += (a*t[i]+b) * (rho_t/data['eta_tilde'+age[i]]) * np.exp(-h_opt['h']/data['A']/data['eta_tilde'+age[i]])
	return z
#%%
fig = plt.figure(figsize=(50, 36))
gs = GridSpec(9, 10, figure=fig)
y=0
for year in range(2014,2023):
	save_path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/at_b/opt_E_h_a033/'
	path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/dataframe_40/'+str(year)+'_40.txt'
	data = pd.read_csv(path,sep=',')
	ai=0
	E_list=[]
	a=np.linspace(0,0.033,10)
	x=0
	for i in range(10):
		# E_ = np.load(save_path+str(year)+'_age_E_a_'+str(ai)+'.npy')
		# E_list.append(E_[-1])
		h_opt = pd.read_csv(save_path+str(year)+'MC_age_h_opt_a_'+str(ai)+'.csv')
		ax = fig.add_subplot(gs[y, x])
		ax.hist(z(data, h_opt, a[ai], b(data,a[ai])))
		
		x+=1
	y+=1
plt.tight_layout()
savefig_path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/figure/z_40_a033/'
# plt.savefig(savefig_path+'14_22_a033.pdf',format='pdf',transparent=True)
plt.show()
# %%
z(data, h_opt, a[ai], b(data,a[ai]))
# %%
t = [45, 55, 65, 75, 85]
age = ['40_49', '50_59', '60_69', '70_79', '80_']	
a=0
b_=b(data,a)
for i in range(5)[:1]:
	rho_t = data['RN'+age[i]] * data['N'] / data['A']
	atb = (a*t[i]+b_) 
	rho_etatilde = (rho_t/data['eta_tilde'+age[i]])
	phi = np.exp(-h_opt['h']/data['A']/data['eta_tilde'+age[i]])
# %%
rho_t
# %%
atb
# %%
rho_etatilde
# %%
phi
# %%
plt.hist(atb*rho_etatilde*phi)
# %%
b_=b(data,a)