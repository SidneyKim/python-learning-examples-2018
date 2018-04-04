import numpy as np

dt = np.array([1,2,3,4,5,6,7], dtype=np.int8)

print(dt)
print(type(dt))
print(dt.dtype)

print(dt[0:4:2])

dt1 = dt*2

print(dt*2)
print(dt+10)
print(dt*dt1)

dt = dt-dt*0.033

print(dt)

nd = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(nd)

for n in nd:
    print(n)

for n in nd[1]:
    print(n)

print(nd[0:2,1])

# 2중 for 대신 nditer 사용
for n in np.nditer(nd):
    print(n)
