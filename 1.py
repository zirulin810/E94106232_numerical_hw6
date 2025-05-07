import numpy as np

A = np.array([
    [1.19,   2.11,  -100,     1   ],
    [14.2,  -0.112,  12.2,   -1   ],
    [0,     100,    -99.9,    1   ],
    [15.3,   0.11,  -13.1,   -1   ]
], dtype=float)

b = np.array([1.12, 3.44, 2.15, 4.16], dtype=float)

x = np.linalg.solve(A, b)

print("(x1, x2, x3, x4) =", x)
