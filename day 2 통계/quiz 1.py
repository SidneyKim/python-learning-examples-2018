from statistics import mean

#csv 읽어와서 통계분석하기
fp = open('./data/crime.csv',mode='r') #read r, write w, append a, tb
data = []
for f in fp:
    #print(f)    
    sList = f.split(',')
    try:
        data.append({
            'pname':sList[0],
            'kill':int(sList[1]),
            'kills':int(sList[2]),
            'kang':int(sList[3]),
            'kangs':int(sList[4])
        })
    except Exception as err:
        pass
fp.close()

#print(data)

#print(data)

# 살인이 가장 많은 서명, 건수
# 평균 살인사건 발생수
# 전체 강도사건 발생 수
# 살인 사건이 10건이상 발생한 서명, 건수

a = max(data, key=lambda n : n['kill'])
print('살인이 가장많은 서명 %(pname)s, 살인발생 건수 %(kill)s'%a)

b = round(mean([ n['kill'] for n in data]),2)
print('평균 살인사건 발생 수 %10.2f'%b)

c = sum([ n['kang'] for n in data])
print('전체 강도사건 발생 수 %10d'%c)

d = list(filter(lambda n : n['kill']>=10, data))
print()
print('살인 10건이상 서명, 건수')

for x in d:
    print('%(pname)8s \t 건수 %(kill)5d'%x)