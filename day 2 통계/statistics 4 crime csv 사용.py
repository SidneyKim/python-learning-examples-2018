#split 
s = 'abc/xxx/yyy'
s = s.split('/')
print(s)


#csv 읽어와서 통계분석하기
fp = open('./data/crime.csv',mode='r') #read r, write w, append a, tb
data = []
for f in fp:
    #print(f)
    sList = f.split(',')
    data.append({
        'pname':sList[0],
        'kill':sList[1],
        'kills':sList[2],
        'kang':sList[3],
        'kangs':sList[4]
    })
fp.close()



#print(data)
# 헤더제거
data.pop(0)

#print(data)

# 살인이 가장 많은 서명, 건수
# 평균 살인사건 발생수
# 전체 강도사건 발생 수
# 살인 사건이 10건이상 발생한 서명, 건수

a = sorted(data, key=lambda n : n['kill'], reverse=True)[0]
print(a)


