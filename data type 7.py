a = 100
a = str(a)
print(a, type(a))

b = '200'
b = int(b)

c = '3.14'
c = float(c)

print(c, type(c))

#immutable -> mutable
d = (10,20,30)
print(d)

d = list(d)
d[1] = 100

print(d)

e = [ 10,20,30,10,10,10]
print(e)

e = set(e)
print(e)