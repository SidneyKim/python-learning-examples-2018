#def 함수명(args(인자들));
# (indent)   구현
a = 1


def fn():
    print('a')
    print('b')
    #a += 1
    print (a)

def sum1(a,b):
    return a+b

fn()
fn()

print(sum1(100,200))


def circle(r):
    return r**2*3.14

print('반지름 %d 원의 면적%f '%(3,circle(3)))


def circle2(r):
    return r, r**2*3.14, r*3.14

print('반지름: %d 원의 면적:%f 원의 지름: %f'%circle2(3))

def fn2(a,b):
    print(a,b)

#명시적 인자 호출
fn2(b=20,a=10)

# default 인자
def fn3(a=1,b=2,c=3):
    print(a,b,c)

fn3()
fn3(a=10)

print('a',1,3,  end='' , sep='/')
print('a',1,3,  end='' , sep='/')

print()

#가변인자

def fn4(*arg):
    print(arg)
    print(type(arg))

fn4([ n for n in range(1,10)],'a')
