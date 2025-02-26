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
# for year in range(2014, 2023):
# 	path = '/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/DSL_data/' + str(year) + '.txt'
# 	data = pd.read_csv(path, sep='\t')
# 	data = data[data['RD40_49'] != 0]
# 	eta = data['h']/data['A']
# 	N_40 = data['N'] * data['RN40_49']
# 	D_40 = data['D'] * data['RD40_49']
# 	phi_40 = D_40/N_40
# 	eta_tilde_40 = eta/-np.log(phi_40)
# 	# 새로운 데이터로 컬럼 값을 업데이트
# 	data['eta_tilde0_49'] = eta_tilde_40
# 	# 컬럼 이름 변경
# 	data.rename(columns={'eta_tilde0_49': 'eta_tilde40_49'}, inplace=True)
# 	# 삭제할 컬럼 지정
# 	columns_to_delete = ['eta_noage', 'eta_age_simul', 'eta_age_th']
# 	# 컬럼 삭제
# 	data.drop(columns=columns_to_delete, inplace=True)
# 	save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/dataframe_40/' + str(year) + '_40.txt'
# 	data.to_csv(save_path, index=False)
# %%
data
# %%

for year in range(2014, 2023)[3:4]:
	path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/raw_data/' + str(year) + '_RNRD.txt'
	data = pd.read_csv(path, sep='\t')
	data = data[data['h'] != 0]
	data = data[data['D'] != 0]
	data = data[data['RD40_49'] != 0]
	eta = data['h']/data['A']
	for age in ['40_49', '50_59', '60_69', '70_79', '80_']:
		N = data['N'] * data['RN'+age]
		D = data['D'] * data['RD'+age]
		phi = D/N
		eta_tilde = eta/-np.log(phi)
		data['eta_tilde'+age] = eta_tilde
	# # 컬럼 이름 변경
	# data.rename(columns={'eta_tilde0_49': 'eta_tilde40_49'}, inplace=True)
	# # 삭제할 컬럼 지정
	# columns_to_delete = ['eta_noage', 'eta_age_simul', 'eta_age_th']
	# # 컬럼 삭제
	# data.drop(columns=columns_to_delete, inplace=True)
	save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/data_over40/' + str(year) + '_40.txt'
	data.to_csv(save_path, index=False)
# %%
import numpy as np
import pandas as pd

for year in range(2014, 2023):
    path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/raw_data/' + str(year) + '_RNRD.txt'
    data = pd.read_csv(path, sep='\t')
    
    # 필터링: 'h', 'D', 'RD40_49' 값이 0이 아닌 경우만 남김
    data = data[data['h'] != 0]
    data = data[data['D'] != 0]
    data = data[data['RD40_49'] != 0]
    
    # eta 계산
    eta = data['h'] / data['A']
    
    for age in ['40_49', '50_59', '60_69', '70_79', '80_']:
        N = data['N'] * data['RN' + age]
        D = data['D'] * data['RD' + age]
        phi = D / N
        
        # phi가 0인 경우는 아예 데이터에서 제거
        data = data[phi > 1e-10]  # phi가 1e-10보다 작은 행 제거
        
        # phi가 0인 행이 제거된 후에 eta와 eta_tilde 다시 계산
        N = data['N'] * data['RN' + age]
        D = data['D'] * data['RD' + age]
        phi = D / N
        
        eta = data['h'] / data['A']  # data가 바뀌었으므로 eta도 재계산
        eta_tilde = eta / -np.log(phi)  # 다시 계산된 phi로 eta_tilde 계산
        
        # 결과 추가
        data['eta_tilde' + age] = eta_tilde
    
    # 저장
    save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/data_over40/' + str(year) + '_40.txt'
    data.to_csv(save_path, index=False)
# %%
