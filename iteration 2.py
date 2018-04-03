s  = 'abcdef'

for n in s:
    print(n)


myL = [10,20,30,40,50,60]

for n in myL:
    print(n)

myDic = {'aaa':1,'bbb':2,'ccc':'x'}

for n in myDic:
    print(n)

for n in myDic.keys():
    print(n)

for n in myDic.values():
    print(n)

for n in myDic.items():
    print(n)

for k,v in myDic.items():
    print(k,v)

for [k,v] in myDic.items():
    print(k,v)

x = range(0,100,1)
print(x)
print(list(x))