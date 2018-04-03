s = { 1,2,3,4,5,5,5,5,5,5,5}

print(s)
print(type(s))

s.add(50)
s.add('a')

print(s)

s.remove(5)

print(s)

s1 = { 10,20,30,40,50}
s2 = {20,30, 1}

print(s1 & s2) #intersect
print(s1 | s2) #union
print( s1 - s2) #minus

