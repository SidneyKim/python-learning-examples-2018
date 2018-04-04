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

#경찰서 별 살인사건을 라인 차트로
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import matplotlib.pyplot as plt


x = [n['pname'] for n in data]
y = [n['kill'] for n in data]
print(x)
print(y)

plt.xticks(rotation=45)
plt.scatter(x,y)
plt.show()
