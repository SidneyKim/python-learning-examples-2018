a = [n for n in range(1,11)]
b = a #shallow copy

c = a.copy()

print('주소가 같다',id(a))
print('주소가 같다',id(b))
print('주소가 다르다',id(c))

b[0] = 100
print(a)

data = [1,2,3,4]

def fn(arg):
    arg[0]=100

print(data)

fn(data)
print(data)

def fn1():
    a = []
    a.append(10)
    a.append(20)
    return a

print(fn1())

#약수 구하기
def yaksu(n):
    return [a for a in range(1,n+1) if n%a==0]

print(yaksu(10))