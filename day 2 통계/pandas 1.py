import pandas as pd
import numpy as np

# 1차원 데이터
sr = pd.Series([10,20,30,40], dtype=np.int8)
sr.index = ['aa','bb','cc','dd']

print(sr)
print(type(sr))

print(sr[0])

print(sr[0:3])

print(sr['bb'])

# 인덱스범위 0 <= x < 1 
print(sr[0:1])

# 인덱스 범위 'aa' <= x <= 'bb 포함됨!!
print('manual index:','\n\r',sr['aa':'bb'])

print('series sum:',sr.sum())

#통계함수
print(sr.mean())
print(sr.std())
print(sr.mean())
print(sr.median())
print(sr.max())
print(sr.min())

# 값이 max 의 index
print(sr.idxmax())

# 연산 가능
print(sr + 2)
print(sr**2)

# boolean index
print(sr > 20)
print(sr[sr>20])
print(sr[sr>20].sum())

# 정렬 후 2개만 추출
print(sr.sort_values()[:2])

