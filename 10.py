def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	r, c = len(vectors), len(vectors[0])
	cov_mat = [[0 for _ in range(r)] for _ in range(r)]
	means = [sum(row) / c for row in vectors]

	for i in range(r):
		for j in range(i, r):
			cov = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(c)) / (c - 1)
			cov_mat[i][j] = cov_mat[j][i] = cov
	return cov_mat