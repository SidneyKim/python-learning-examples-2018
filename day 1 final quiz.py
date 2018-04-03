""" 1. 키와 몸무게를 입력받아
 비만도를 구하고 결과를 출력하시요
표준체중(kg)={신장(cm)-100}×0.85
비만도(%)=현재체중/표준체중(%)×100

비만도가90%이하
저체중,
90초과 ~∼110%
정상,
110초과~120%
과체중,
120%초과 
비만 
"""
print('문제1')

def get_obst(h,w):
    stdWeight = (h-100)*0.85
    return w/stdWeight*100

def get_category(arg):    
    if arg > 120:
        return '비만'
    elif arg > 110:
        return '과체중'
    elif arg > 90:
        return '정상'
    else:
        return '저체중'
obst = get_obst(183,71)
cat = get_category(obst)

print('비만도:%0.2f 분류:%s'%(obst,cat))

print()

print('문제2')
"""
2. 하나의 연도를 입력받아 윤년 여부를 출력하시요
(윤년조건 
1) 4로 나누어 떨어지지만 100으로 나눠떨어지면 않됨
2) 400 으로 나눠 떨어지면 윤년
"""

def isYunYear(y):
    if y%4 == 0 and y%100 != 0:
        return '윤년'
    else:
        if y%400 == 0:
            return '윤년'
        else:
            return '윤년아님'
        
a = 2018

print(isYunYear(a))
print()


"""
3. 1~100까지 섭씨 온도에 대한 각각에 대한 화씨온도를 출력하시요
----------------------
	섭씨	화씨
-----------------------
	1         ??
	2         ?
	....
	100       ?
"""
print('문제3')
#(섭씨온도 × 1.8) + 32 = 화씨온도

arr = range(1,101)

print('%10s %6s'%('섭씨','화씨'))
print('--------------------------')
for n in arr:
    print('%10d %10.2f'%(n, (n*1.8)+32))


print()
"""
4. 다음의 연봉데이터가 있다 세금 3.3을 제한 
실수령액 리스트와 총합, 평균을 구하시요
data=[1000,2000,3000,4000,5000,6000]
"""
print('문제4')
sal = [1000,2000,3000,4000,5000,6000]
taxRate = 3.3/100

realSal = [n-n*taxRate for n in sal]
print('실수령액:',realSal)

sumSal = sum(realSal)
avgSal = sum(realSal)/len(realSal)

print('총합:%10.2f \t 평균:%10.2f'%( sumSal, avgSal))

print()

"""
5. 장비명, 갯수, 단가을 입력받아 출력하시요
1)입력양식
장비명:
갯수:
단가:
계속입력(y/n):
n 할때 까지의 데이터 출력
2) 출력양식
----------------------------------------
	장비명	갯수	단가	가격
-------------------------------------
 """


print('문제5')

yesNo = 'y'

dic = []

#입력부
while yesNo == 'y':
    
    name = input('장비명:')
    qty = float(input('갯수:'))
    unitPrice = float(input('단가:'))
    amount = qty * unitPrice

    dic.append({'name':name, 'qty':qty, 'unitPrice':unitPrice, 'amount':amount})
    
    yesNo = input('계속입력(y/n):')    

#출력부    
text = """
----------------------------------------
	장비명 	 갯수	  단가	  가격
----------------------------------------
"""
print(text)

for x in dic:
    #print(x)
    print('%(name)10s %(qty)10d %(unitPrice)10.2f %(amount)10.2f'%x)
