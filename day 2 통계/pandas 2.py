import pandas as pd
import numpy as np

df = pd.DataFrame([[10,20,30],[1,3,1],[9,3,5],[12,55,1]])

df2 = pd.DataFrame([[10,20,30],[1,3,1],[9,3,5],[12,55,1],[1,1,1]],
        index = ['a','b','c','d','x'],
        columns = ['kor','eng','math'])

#df2.columns=['a','b','c']

print(df)
print(type(df))

print(df2)

# 리스트 + 딕셔너리로 DataFrame 생성
df = pd.DataFrame([{'name':'hyunju','age':20},{'name':'jong su','age':60}])

print(df)

print(df[1:])


print(df2[['kor','math']])

# ix 속성 사용하여 슬라이싱
print(df2.ix[1:])

print(df2.ix[1:,'eng':])

print(df2.ix[0:2,['kor','math']])