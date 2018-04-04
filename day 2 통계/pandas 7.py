import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame([[10,20,30],[1,3,1],[9,3,5],[12,55,1],[1,1,1]],
        index = ['김광성','김현주','권종수','김학필','강부근'],
        columns = ['kor','eng','math'])

print(df)
print('='*60)
'''
1. 권종수의 국,영,수 합계/평균
'''
print('합계:%8d, 평균:%8d'%(df.ix['권종수'].sum(),df.ix['권종수'].mean()))

print('='*60)
'''
2. 국어 점수 합계/평균
'''
print('국어 점수 합계:%8d, 평균:%8.2f '%(df['kor'].sum(),df['kor'].mean()))

print('='*60)
'''
3. 전체 점수의 합계/평균
'''


print('전체접수 합계:%8d, 평균:%8.2f'%(df.sum().sum(),df.sum().mean()))

print('='*60)
'''
4. 국어, 영어, 수학의 가장 높은 점수
'''

print(df.max())

print('='*60)
'''
5. 국어 점수 탑 2개
'''

print(df['kor'].nlargest(2))

print('='*60)