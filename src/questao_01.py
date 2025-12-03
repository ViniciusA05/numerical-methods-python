import numpy as np

def gauss_pivot(A):
    n = len(A)
    
    for i in range(n):
        pivot = np.argmax(np.abs(A[i:, i])) + i
        A[[i, pivot]] = A[[pivot, i]]
        
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (A[i, -1] - np.dot(A[i, i:-1], x[i:])) / A[i, i]
        
    return x

if __name__ == '__main__':
    A = np.array([
        [0.0, -3.0, 7.0, 2.0],
        [1.0, 2.0, -1.0, 3.0],
        [5.0, -1.0, 0.0, 2.0]
    ])
    
    sol = gauss_pivot(A.copy())
    
    print("Sistema de Equações:")
    print("0x1 - 3x2 + 7x3 = 2")
    print("1x1 + 2x2 - 1x3 = 3")
    print("5x1 - 1x2 + 0x3 = 2")
    print("\nSolução (x1, x2, x3):")
    print(sol)