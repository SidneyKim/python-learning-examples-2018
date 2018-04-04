list3 = [{'name':'김현주','kor':51,'eng':31},
 {'name':'김광성','kor':78,'eng':87}, 
 {'name':'김일한','kor':45,'eng':87}, 
 {'name':'권종수','kor':11,'eng':22}]

list2 = [('김현주',50,90),('김광성',10,20),('김일한',51,33),('권종수',51,10)]
list1 = list(range(1,101))

# sum, max, min  내장함수

print(max(list1))
print(sum(list1))

print(max(list2, key=lambda n:n[1]))
print(sum([n[1] for n in list2])) # sum 은 key 인수가 없음

print(min(list3, key=lambda n:n['kor']))
print(sum([n['kor'] for n in list3]))

# 20보다 큰 값 찾기
f = filter(lambda n: n> 20, list1)

print(list(f))

# 특정 스트링이 들어간 것 찾기
x = filter(lambda k: '종' in k['name'], list3)

print(list(x))

