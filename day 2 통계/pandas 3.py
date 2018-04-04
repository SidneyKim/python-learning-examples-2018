import pandas as pd
import numpy as np

# 컬럼 단위 데이터 구성
df = pd.DataFrame()
df['col1']=[10,20,30]
df['col2']=df['col1']*10
df['col3']=df['col2']*2
df['col4']=df['col3']%3

print(df)

# 행단위 

df2 = None
df2 = pd.DataFrame(columns = ['kor','eng','math'])

df2.at[0] = [10,20,10]

print(df2[0:1]*2)

#df2.at[1] = pd.Series(df2[0:1]*1.2)
df2.at['a'] = [1,2,3]

print(type(df2[0:1]))

'''
df2.at[2] = df2.at[1]*2
df2.at[3] = df2.at[2]%3
df2.at[4] = df2.at[3]//2
df2.at[5] = df2.at[4]*8
df2.at[6] = df2.at[5]//3
'''
print(df2)


