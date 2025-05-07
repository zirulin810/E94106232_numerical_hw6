def crout_tridiag(a, b, c):
    n = len(a)
    L_diag = [0.0]*n
    U_sup  = [0.0]*n

    L_diag[0] = a[0]
    U_sup[0]  = c[0] / L_diag[0]

    for i in range(1, n):
        L_diag[i] = a[i] - b[i] * U_sup[i-1]
        if i < n-1:
            U_sup[i] = c[i] / L_diag[i]
    return L_diag, U_sup

def solve_tridiag_crout(a, b, c, d):
    n = len(d)
    L_diag, U_sup = crout_tridiag(a, b, c)

    y = [0.0]*n
    y[0] = d[0] / L_diag[0]
    for i in range(1, n):
        y[i] = (d[i] - b[i]*y[i-1]) / L_diag[i]

    x = [0.0]*n
    x[-1] = y[-1]
    for i in range(n-2, -1, -1):
        x[i] = y[i] - U_sup[i]*x[i+1]

    return x

a = [3, 3, 3, 3]
b = [0, -1, -1, -1]
c = [-1, -1,  1,  0]
d = [2, 3, 4, 1]

x = solve_tridiag_crout(a, b, c, d)
print("x ≈", [round(xi, 6) for xi in x])
