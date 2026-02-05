def function(x):
    return x**3-x-1

a,b=0,3

def bijection(f,a,b,tol=1e-6,max_iter=100):
    
    if f(a)*f(b)>=0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for i in range(max_iter):
        c=(a+b)/2
        if abs(f(c))<tol or (b-a)/2<tol:
            return c,i
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
    return c,max_iter

root,iteration=bijection(function,a,b)
print(f"Approximate root:{root:.6f}")
print(f"found in {iteration} iterations")
print(f"function value at root: {function(root):.6f}")
    
        