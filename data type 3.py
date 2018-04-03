
a = [0,1,1,2,3,4,5]

print(a)
print(type(a))

print(a[0:4:2])

a[0] = 100

print(a)

a.append(999)

print(a)

a.insert(1,1000)
a.remove(999)
#a.pop(3) #index remove


print(a)

print(a.count(1))

print(len(a))