import matplotlib.pyplot as plt 
def function(x,y):
    return  (y-x)/(y+x)


def meuler_method(f,xo,b,yo,n):
    h=(b-xo)/n
    xold=[xo]
    yold=[yo]

    for i in range (n):
        ys=yold[-1]+h*f(xold[-1],yold[-1])
        xp=xold[-1]+h
        yn=yold[-1]+h*(f(xold[-1],yold[-1])+f(xp,ys))/2
        xn=xold[-1]+h
        xold.append(xn)
        yold.append(yn)
    return xold,yold

xo=0
b=0.1
yo=1
n=5

(xv,yv)=meuler_method(function,xo,b,yo,n)
print(xv,yv)

plt.plot(xv,yv)
plt.show()