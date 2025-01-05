#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
plt.rcParams['mathtext.fontset'] = 'cm'
from matplotlib.gridspec import GridSpec
plt.rcParams['font.family'] = 'Helvetica'
#%%
for year in range(2014, 2023):
    # year=2014
    path_N='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_N.csv'
    path_D='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_D.csv'
    path='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/DSL_data/'+str(year)+'.txt'
    data_age_N = pd.read_csv(path_N)
    data_age_D = pd.read_csv(path_D)
    data = pd.read_csv(path,sep='\t')
    
    RNage_list_49= ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    RN = [np.mean(data[RNage_list_49].sum(axis=1))]
    for t in ['50_59', '60_69', '70_79', '80_']:
        RN.append(np.mean(data['RN'+t]))
    phi=[]
    N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    for t in ['0_49', '50_59', '60_69', '70_79', '80_']:
            eta_i = data['h']/data['A']
            if t=='0_49': N_it=N_49
            else: N_it=data['N']*data['RN'+t]
            phi.append(np.mean(np.exp(-eta_i/data['eta_tilde'+t])))


    
    save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/fig_N_phi_as_age/'
    fig = plt.figure(figsize=(10, 4))
    # GridSpec 객체 생성: 1행 2열
    gs = GridSpec(1, 2, figure=fig)
    # 첫 번째 서브플롯
    ax1 = fig.add_subplot(gs[0, 0])  # 첫 번째 열
    ax1.plot(['0_49', '50_59', '60_69', '70_79', '80_'], RN, marker='o')  # 샘플 데이터
    ax1.set_ylabel(r'$\langle N\rangle_i$',size=20)
    ax1.set_xlabel('age',size=20)
    ax1.set_ylim(0.14, 0.41)
    # 두 번째 서브플롯
    ax2 = fig.add_subplot(gs[0, 1])  # 두 번째 열
    ax2.plot(['0_49', '50_59', '60_69', '70_79', '80_'], phi, marker='o') 
    ax2.set_ylabel(r'$\langle \phi\rangle_i$',size=20)
    ax2.set_xlabel('age',size=20)
    ax2.set_ylim(0,0.25)
    # 레이아웃 조정 및 출력
    plt.tight_layout()
    plt.savefig(save_path+str(year)+'.pdf',format='pdf',transparent=True)
    plt.show()
    # %%
