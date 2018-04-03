data = [('홍길동',79,89,90),('김현주',10,20,10),('김광성',90,80,100)]
print(data)


print(sum([1,2,3]))

for n,k,e,m in data:
    print("이름:%s 국어:%d, 영어:%d, 수학:%d"%(n,k,e,m))

print("국어점수 합계:%d"%(sum([n[1] for n in data])))


data2 = [{'name':'홍길동','kor':79,'eng':89,'math':90}
,{'name':'김현주','kor':11,'eng':22,'math':55}
,{'name':'김광성','kor':80,'eng':90,'math':76}
]

print (data2)

for dt in data2:
    print('이름:%(name)8s 국어:%(kor)4d 영어:%(eng)4d 수학:%(math)4d'%dt)

print("국어점수합계:%5d"%sum([n['kor'] for n in data2]))