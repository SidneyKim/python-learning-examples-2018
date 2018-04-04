import numpy as np

dt1 = np.array([1,2,3,40,50,5,6,7])
dt2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.sum(dt1))
print(np.sum(dt2))
# 1열만 합계
print(np.sum(dt2[:,1]))

print(dt2[:,1])

# 평균
print(np.mean(dt1))
print(np.mean(dt2))

# 중앙값
print(np.median(dt1))
print(np.median(dt2))

print(np.percentile(dt1, 31))

#분산
print(np.std(dt1))

#최대값
print(np.max(dt2))
print(np.max(dt2[:,1]))

# 조건에 맞는 튜플 반환, 각 행에서 가장 큰 값
print(np.max(dt2, axis=1))
# 각 열에서 가장 큰 값
print(np.max(dt2, axis=0))

# max 값의 인덱스
print(np.argmax(dt1))

# 조건에 맞는 인덱스 반환
print(np.where(dt1 > 4)[0])

b = np.array([True,False,True,False,True,True,False,False])

#boolean index
print(dt1[b])

print(dt1*b)

print(dt1 > 5)
# 조건에 맞는 값 반환
print(dt1[dt1>5])


