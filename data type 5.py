a = {'a':100, 'b':'x', "c": "100"}

print (a)
print(type(a))

print(type(a.keys()))

a['a'] = 'abc'

print(a)

a['x'] = 'xxx'

print(a)

print(a.values())
print(a.items())

a.pop('a')

print(a)



