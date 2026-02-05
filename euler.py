import matplotlib.pyplot as plt
import numpy as np

def function(x,y):
    return 2+(x*y)**0.5


def euler_method(f,xo,b,yo,n):
    h=(b-xo)/n
    xold=[xo]
    yold=[yo]
    for i in range (n):
        yn=yold[-1] +h*f(xold[-1],yold[-1])
        xn= xold[-1] + h
        
        xold.append(xn)
        yold.append(yn)
    return xold,yold
        
def g(x):
    return np.exp(x+(x**3)/3)



xo=1
b=2
yo=1
n=10

(xv,yv)=euler_method(function,xo,b,yo,n)

print(xv,yv)

yext=[g(x) for x in xv]

plt.plot(xv,yv, label='Euler Approximation')
plt.plot(xv,yext, label='Exact Solution')
plt.legend()
plt.show()