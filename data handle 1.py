# 문자열 concat 가능
s = 'abc'
s = s + 'def'
print(s)

print('xxx'+'aaa')

# 문자열 곱셈 가능 (n회 반복)
s = s*3
print(s)

a = 10
b = 3.14
c = 'abc'
s = 'a=%10d b=%10.2f c=%s'%(a,b,c)
print(s)

dic = {'name':'김현주','age':37}
print('이름:%(name)s 나이:%(age)d'%dic)
