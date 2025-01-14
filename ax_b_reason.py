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
    # path_N='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_N.csv'
    # path_D='/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/'+str(year)+'_extract_D.csv'
    path='/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/dataframe_40/'+str(year)+'_40.txt'
    # data_age_N = pd.read_csv(path_N)
    # data_age_D = pd.read_csv(path_D)
    data = pd.read_csv(path,sep=',')
    # RNage_list_49 = ['RN0_9', 'RN10_19', 'RN20_29', 'RN30_39', 'RN40_49']
    RN = []
    D = []
    for t in ['40_49', '50_59', '60_69', '70_79', '80_']:
        # RN.append(np.mean(data['N']*data['RN'+t]))
        # RN.append(sum(data['N']*data['RN'+t]))
        D.append(np.mean(data['D']*data['RD'+t]))
    phi=[]
    
    # N_49 = data['N']* data[RNage_list_49].sum(axis=1)
    for t in ['40_49', '50_59', '60_69', '70_79', '80_']:
            eta_i = data['h']/data['A']
            # if t=='0_49': N_it=N_49
            N_it=data['N']*data['RN'+t]
            phi.append(np.mean(np.exp(-eta_i/data['eta_tilde'+t])))


    
    save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/fig_N_phi_as_age/'
    fig = plt.figure(figsize=(10, 4))
    # GridSpec 객체 생성: 1행 2열
    gs = GridSpec(1, 2, figure=fig)
    # 첫 번째 서브플롯
    ax1 = fig.add_subplot(gs[0, 0])  # 첫 번째 열
    # ax1.plot(['40_49', '50_59', '60_69', '70_79', '80_'], RN, marker='o')  # 샘플 데이터
    ax1.plot(['40_49', '50_59', '60_69', '70_79', '80_'], D, marker='o')  # 샘플 데이터
    # ax1.set_ylabel(r'$\langle N\rangle_i$',size=20)
    ax1.set_ylabel(r'$\langle D\rangle_i$',size=20)
    ax1.set_xlabel('age',size=20)
    # ax1.set_ylim(0, 41)
    # 두 번째 서브플롯
    ax2 = fig.add_subplot(gs[0, 1])  # 두 번째 열
    ax2.plot(['40_49', '50_59', '60_69', '70_79', '80_'], phi, marker='o') 
    ax2.set_ylabel(r'$\langle \phi\rangle_i$',size=20)
    ax2.set_xlabel('age',size=20)
    ax2.set_ylim(0,0.25)
    # 레이아웃 조정 및 출력
    plt.tight_layout()
    plt.savefig(save_path+str(year)+'.pdf',format='pdf',transparent=True)
    plt.show()
# %%

"""
over 40 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
plt.rcParams['mathtext.fontset'] = 'cm'
from matplotlib.gridspec import GridSpec
plt.rcParams['font.family'] = 'Helvetica'

for year in range(2014, 2023):
    # year=2014
    # print(year)
    path_N = '/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/' + str(year) + '_extract_N.csv'
    path_D = '/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/2023_rate_extract_DSL/' + str(year) + '_extract_D.csv'
    path = '/home/users/YongsungKwon/workplace/Yongpyter/dataset/tuberculosis/data/DSL_data/' + str(year) + '.txt'
    data_age_N = pd.read_csv(path_N)
    data_age_D = pd.read_csv(path_D)
    data = pd.read_csv(path, sep='\t')

    # 0~29, 30~49 세 구간으로 수정
    RNage_list_29 = ['RN0_9', 'RN10_19', 'RN20_29']  # 0~29세 구간
    RDage_list_29 = ['RD0_9', 'RD10_19', 'RD20_29']  # 0~29세 구간
    RNage_list_39 = ['RN30_39']  # 0~29세 구간
    RDage_list_39 = ['RD30_39']  # 0~29세 구간
    RNage_list_49 = ['RN40_49']  # 30~49세 구간
    RDage_list_49 = ['RD40_49']  # 30~49세 구간

    RN = [np.mean(data[RNage_list_29].sum(axis=1)), np.mean(data[RNage_list_39].sum(axis=1)), np.mean(data[RNage_list_49].sum(axis=1))]  # 0~29세와 30~49세의 평균
    RD = [np.mean(data[RDage_list_29].sum(axis=1)), np.mean(data[RDage_list_39].sum(axis=1)), np.mean(data[RDage_list_49].sum(axis=1))]  # 0~29세와 30~49세의 평균

    # 이후 50~59, 60~69, 70~79, 80~의 나머지 연령대 추가
    for t in ['50_59', '60_69', '70_79', '80_']:
        RN.append(np.mean(data['RN' + t]))
        RD.append(np.mean(data['RD' + t]))

    phi = []
    N_29 = data['N'] * data[RNage_list_29].sum(axis=1)
    D_29 = data['D'] * data[RDage_list_29].sum(axis=1)
    N_39 = data['N'] * data[RNage_list_39].sum(axis=1)
    D_39 = data['D'] * data[RDage_list_39].sum(axis=1)
    N_49 = data['N'] * data[RNage_list_49].sum(axis=1)
    D_49 = data['D'] * data[RDage_list_49].sum(axis=1)
    phi_29 = D_29 / N_29
    phi_39 = D_39 / N_39
    phi_49 = D_49 / N_49
    eta_i = data['h'] / data['A']

    for t in ['0_29','30_39', '40_49', '50_59', '60_69', '70_79', '80_']:
        if t == '0_29':
            N_it = N_29
            e_tilde = eta_i / (-np.log(phi_29))
            phi.append(np.mean(np.exp(-eta_i / e_tilde)))
        elif t == '30_39':
            N_it = N_39
            e_tilde = eta_i / (-np.log(phi_39))
            phi.append(np.mean(np.exp(-eta_i / e_tilde)))
        elif t == '40_49':
            N_it = N_49
            e_tilde = eta_i / (-np.log(phi_49))
            phi.append(np.mean(np.exp(-eta_i / e_tilde)))
        else:
            N_it = data['N'] * data['RN' + t]
            phi.append(np.mean(np.exp(-eta_i / data['eta_tilde' + t])))

    save_path = '/home/users/YongsungKwon/workplace/Yongpyter/Tuberculosis_hospital_optimization/data_result/fig_N_phi_as_age/'
    fig = plt.figure(figsize=(10, 4))

    # GridSpec 객체 생성: 1행 2열
    gs = GridSpec(1, 2, figure=fig)

    # 첫 번째 서브플롯
    ax1 = fig.add_subplot(gs[0, 0])  # 첫 번째 열
    ax1.plot(['0_29','30_39', '40_49', '50_59', '60_69', '70_79', '80_'], RN, marker='o')  # 샘플 데이터
    ax1.set_ylabel(r'$\langle N\rangle_i$', size=20)
    ax1.set_xlabel('age', size=20)
    ax1.set_ylim(0, 0.41)

    # 두 번째 서브플롯
    ax2 = fig.add_subplot(gs[0, 1])  # 두 번째 열
    ax2.plot(['0_29','30_39', '40_49', '50_59', '60_69', '70_79', '80_'], phi, marker='o')
    ax2.set_ylabel(r'$\langle \phi\rangle_i$', size=20)
    ax2.set_xlabel('age', size=20)
    ax2.set_ylim(0, 0.25)

    # 레이아웃 조정 및 출력
    plt.tight_layout()
    plt.savefig(save_path + str(year) + '_49.pdf', format='pdf', transparent=True)
    plt.show()
    plt.close()


    columns = ['RD0_9', 'RD10_19', 'RD20_29', 'RD30_39', 'RD40_49']
    zero_counts = {col: (data[col] == 0).sum() for col in columns}
    print(zero_counts)
# %%
data
# %%
