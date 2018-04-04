list3 = [{'name':'김현주','kor':51,'eng':31},
 {'name':'김광성','kor':78,'eng':87}, 
 {'name':'김일한','kor':45,'eng':87}, 
 {'name':'권종수','kor':11,'eng':22}]

list2 = [('김현주',50,90),('김광성',10,20),('김일한',51,33),('권종수',51,10)]
list1 = list(range(1,101))

# map 내장함수 , list 각 요소를 변경
m = map(lambda n : n*10, list1)
print(m)
print(list(m))

# sorted 
s = sorted(list1, reverse=True)
print(s)

s = sorted(list3, key=lambda k:k['eng'])
print(s)


