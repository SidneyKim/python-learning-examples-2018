
#하나의 정수를 입력 받아 짝수면 '짝' 홀수면 '홀' 출력

a = input('정수:')
a = int(a)
n = '짝' if a%2==0 else '홀'
print(n)