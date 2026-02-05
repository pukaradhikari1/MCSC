def function(x):
    return x**3-x-1

def false_position(f,x0,x1,tol=1e-6,max_iter=100):
    for i in range(max_iter):
        fx0=f(x0)
        fx1=f(x1)
        
        if fx0*fx1>=0:
            raise ValueError("f(x0) and f(x1) must have opposite signs")
        if abs(fx1)<tol:
            return x1,i
        c=x1-fx1*(x1-x0)/(fx1-fx0)
        if fx0 * f(c) < 0:
            x1 = c
        else:
            x0 = c
    return x1,max_iter
root,iteration=false_position(function,0,3)
print(f"Approximate root:{root:.6f}")
print(f"found in {iteration} iterations")