import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    for it in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i, i]
        
        # Check convergence
        if np.linalg.norm(x - x_old) < tol:
            print(f"Converged in {it} iterations")
            return x
    
    print(f"Max iterations ({max_iter}) reached")
    return x