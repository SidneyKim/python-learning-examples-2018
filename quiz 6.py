#10의 약수를 구하시오

a = 10

x = range(1,a+1)

print(x)

for n in x:
    if a%n==0:
        print(n)        
