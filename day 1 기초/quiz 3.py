#하나의 점수를 읽어 
#90~100 : A ...
#나머지 F


#a = input('점수:')
a = 10
a = float(a)
x = "결과"

if 100 >= a >= 90:
    p = 'A'
elif a >= 80:
    p = 'B'
elif a >= 70:
    p = 'C'
elif a >= 60:
    p = 'D'
else:
    p = 'F'

#print ('학점은:',p)

# 딕셔너리로 switch case 구현
dic = {10:'A',9:'A',8:'B',7:'C',6:'D'}

result = dic.get(61//10,'F')

print(result)





