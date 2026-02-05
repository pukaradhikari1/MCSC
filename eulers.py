        
def function(x,y):
    return y*(1+ x**2)


def euler_method(f,a,b,yo,n):
    h=(b-a)/n
    xo=a
    yold=yo
    for i in range (n):
        yn=yold +h*f(xo,yold)
        yold=yn
        xo=xo+h
        print(xo, "\t", yold)
        
        


a=0
b=2
yo=1
n=4

euler_method(function,a,b,yo,n)