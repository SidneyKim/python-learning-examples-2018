#import statistics as st
#from statistics import mean, median
from statistics import *

list3 = [{'name':'김현주','kor':51,'eng':31},
 {'name':'김광성','kor':78,'eng':87}, 
 {'name':'김일한','kor':45,'eng':87}, 
 {'name':'권종수','kor':11,'eng':22}]


# 평균
print(mean((1,2,3)))

# 중간값 (짝수개면 가운데 두개의 평균값)
print(median((1,2,3,5,100,0,3,4,4,4,4,4)))

print(median([n['kor'] for n in list3]))

#표준편차
stdv = stdev([n['kor'] for n in list3])
print(stdv)

