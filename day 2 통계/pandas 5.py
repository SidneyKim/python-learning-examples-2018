import pandas as pd
import numpy as np

df = pd.read_csv('./data/crime.csv',engine='python')

#print(df)


#print(df.max())


#print('최다 살인발생 %8d 건'%df.max()['살인 발생'])

print('최다 살인발생 %7s '%df.ix[df['살인 발생'].idxmax()]['관서명'])
print('최다 살인발생 %8d 건'%df.ix[df['살인 발생'].idxmax()]['살인 발생'])

print('평균 살인발생 %8.2f 건'%df['살인 발생'].mean())
print('전체 강도사건 %8.2f 건'%df['강도 발생'].sum())

#print( df['살인 발생'] > 10)
#print(df['살인 발생'][ df['살인 발생'] > 10])
#print(type(df['살인 발생'][ df['살인 발생'] > 10].index))

for n in df['살인 발생'][ df['살인 발생'] > 10].index:
    #print(n)
    print('관서명: %(관서명)s 발생건수: %(살인 발생)8d 건'%df.ix[n,['관서명','살인 발생']])


import matplotlib.pyplot as mplot

mplot.plot(df['관서명'],df['살인 발생'])
mplot.show()