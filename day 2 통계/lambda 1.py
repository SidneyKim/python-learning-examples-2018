
# 일급함수, first class function
# 함수 참조가능
def show():
    print('show')

def fn(a):
    a()

fn(show)

# 람다 식
a = lambda a,b:a+b

print(a(1,2))

list = list(range(1,101))

print(list)

#가장 큰값 구하기
def fn_max(list):
    a = None
    for n in list:
        if a == None or a < n:
            a = n
            
    return a

print(fn_max(list))

# 리스트 튜플, 국어점수 max 구하기
list2 = [('김현주',50,90),('김광성',10,20),('김일한',51,33),('권종수',51,2810)]

def fn_max_kor(list):
    a = None
    for n in list:
        if a == None or a[1] < n[1]:
            a = n
            
    return a

print(fn_max_kor(list2))

# 리스트 딕셔너리 min 구하기
list3 = [{'name':'김현주','kor':51,'eng':31},
 {'name':'김광성','kor':78,'eng':87}, 
 {'name':'김일한','kor':45,'eng':87}, 
 {'name':'권종수','kor':11,'eng':22}]

def fn_max_dic(list):
    a = None
    for n in list:
        if a == None or a['kor'] < n['kor']:
            a = n
            
    return a

print(fn_max_dic(list3))

# 3개의 함수 일반화 하여 하나로 만들기
# 람다를 활용

def fn_max_gen(list, key):
    a = None
    for n in list:
        if a == None or key(a) < key(n):
            a = n
            
    return a

print(fn_max_gen(list, lambda n:n))
print(fn_max_gen(list2, lambda a:a[1]))
print(fn_max_gen(list3, lambda a:a['kor']))