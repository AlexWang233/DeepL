def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'column':
		matrix = [list(i) for i in zip(*matrix)]

	ans = []
	for i in matrix:
		ans.append(sum(i) / len(i))

	return ans