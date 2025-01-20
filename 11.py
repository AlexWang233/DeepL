import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	diag = np.diag(A)
	nda = A - np.diag(diag)
	cur = np.zeros(len(b))
	temp = cur.copy()
	for _ in range(n):
		for i in range(len(A)):
			temp[i] = (1 / diag[i]) * (b[i] - sum(nda[i] * cur))
		cur = temp.copy()
	return np.round(cur, 4).tolist()