import matplotlib.pyplot as plt 
import numpy as np

def function(x,y):
   return y*(1+ x**2)

def rk2_method(f,xo,b,yo,n):
    h=(b-xo)/n
    xold=[xo]
    yold=[yo]
    for i in range (n):
        k1=h*f(xold[-1],yold[-1])
        k2=h*f(xold[-1]+h,yold[-1]+k1)
        yn=yold[-1] + (1/2)*(k1 + k2)
        xn= xold[-1] + h
        
        xold.append(xn)
        yold.append(yn)
    return xold,yold

def g(x):
    return np.exp(x+(x**3)/3)

xo=0
b=2
yo=1
n=100
(xv,yv)=rk2_method(function,xo,b,yo,n)

yext=[g(x) for x in xv]

plt.plot(xv,yv, label='Euler Approximation')
plt.plot(xv,yext, label='Exact Solution')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()