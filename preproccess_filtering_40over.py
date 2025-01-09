#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
plt.rcParams['mathtext.fontset'] = 'cm'
from matplotlib.gridspec import GridSpec
plt.rcParams['font.family'] = 'Helvetica'
# %%
for year in range(2014, 2023):
	path = '/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/DSL_data/' + str(year) + '.txt'
	data = pd.read_csv(path, sep='\t')
	data = data[data['RD40_49'] != 0]
	eta = data['h']/data['A']
	N_40 = data['N'] * data['RN40_49']
	D_40 = data['D'] * data['RD40_49']
	phi_40 = D_40/N_40
	eta_tilde_40 = eta/-np.log(phi_40)
	# 새로운 데이터로 컬럼 값을 업데이트
	data['eta_tilde0_49'] = eta_tilde_40
	# 컬럼 이름 변경
	data.rename(columns={'eta_tilde0_49': 'eta_tilde40_49'}, inplace=True)
	# 삭제할 컬럼 지정
	columns_to_delete = ['eta_noage', 'eta_age_simul', 'eta_age_th']
	# 컬럼 삭제
	data.drop(columns=columns_to_delete, inplace=True)
	save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/dataframe_40/' + str(year) + '_40.txt'
	data.to_csv(save_path, index=False)
# %%
data
# %%
