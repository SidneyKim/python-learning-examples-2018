import pandas as pd
import numpy as np

df = pd.DataFrame([[10,20,30],[1,5,2],[5,5,5]])

df.index = ['a','b','c']
df.columns = ['kor','eng','math']
print(df)

# 컬럼 별 합계
print(df.sum())
print(type(df.sum())) #series object
print(df.sum().sum())

# 각종 통계 정보를 DataFrame 으로 컬럼별 표현
print(df.describe())

print(df.describe().ix[0])

print(df['kor'])

print(df.index)
print(df.columns)

# ndarray 반환
print(df.values)

print(df > 5)

#df.to_csv('a.csv')

for idx, sr in df.iterrows():
    print(sr)
    print(type(sr))
    print(idx, '%(kor)d %(eng)d %(math)d'%sr)
    