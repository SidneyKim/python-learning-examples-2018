import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/cctv.csv')

print(df)
print('-'*20)


'''
1. 강서구 cctv 년도별 현황을 출력
====================
    2013    2014    2015    2016

'''
print('='*60)
#print( df[ df['기관명'] =='강서구'].index)
print(df.ix[df[ df['기관명'] =='강서구'].index])

'''
2. 2016년 cctv 전체 합계와 평균
'''

#print(df['2016년'].mean())
print('='*60)
print('2016년 cctv 합계%8d, 평균%8d'%(df['2016년'].sum(),df['2016년'].mean()))

'''
3. 강북구, 광진구, 도봉구 년도별 cctv 현황 출력
'''
print('='*60)
#print(df['기관명'])
print(df[ df['기관명'].isin( ['강북구','광진구','도봉구'])])

'''
4. cctv 상위 5개 데이터 출력
'''
print('='*60)
#print(df.ix[:,1:6].values)
print(df.ix[df['소계'].nlargest(5).index])

