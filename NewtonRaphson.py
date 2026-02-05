def function(x):
    return x**3-x-1
def derivative(x):
    return 3*x**2-1

a=1

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, i
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x = x - fx/dfx
    return x, max_iter
root,iteration=newton_raphson(function,derivative,a)
print(f"Approximate root:{root:.6f} ")
print(f"found in {iteration} iteration")
print(f"function value at root: {function(root):.6f}")
