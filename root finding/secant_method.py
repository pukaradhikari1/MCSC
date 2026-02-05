def function(x):
    return x**3-x-1

def secant_method(f,x0,x1,tol=1e-6,max_iter=100):
    for i in range(max_iter):
        fx0=f(x0)
        fx1=f(x1)
        if abs(fx1)<tol:
            return x1,i
        if fx1==fx0:
            raise ValueError("Function values at x0 and x1 are the same. No solution found.")
        x2=x1-fx1*(x1-x0)/(fx1-fx0)
        x0,x1=x1,x2
    return x1,max_iter

root,step=secant_method(function,0,3)
print(f"The approxiamte root is:{root:.6f}")