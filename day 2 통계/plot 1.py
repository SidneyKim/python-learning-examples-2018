from random import * 
import matplotlib.pyplot as plt

y = [randint(1,100),randint(1,100),randint(1,100),randint(1,100)]
x = ['aa','bb','cc','dd']

plt.plot(x,y)
plt.show()

plt.bar(x,y)
plt.show()