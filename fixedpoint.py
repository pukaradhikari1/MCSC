
def fixed_point(g,x0,tol=1e-6,max_iter=100):
    x=x0
    for i in range(max_iter):
        x_new=g(x)
        if abs(x_new-x)<tol:
            return x_new,i
        x=x_new
    return x,max_iter

def g(x):
    return (x+1)**(1/3)

a=1

root,iteration=fixed_point(g,a)
print(f"Approximate root:{root:.6f}")
print(f"found in {iteration} iterations")