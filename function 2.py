def fn():
    print('fn call')

fn1 = fn
print(id(fn), id(fn1))

fn1()
fn()

# switch 문 대체 (함수 호출까지)

def my1():
    print('my 1')

def my2():
    print('my 2')

dic = {0:my1, 2:my2}

dic[0]()