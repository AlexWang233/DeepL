def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	ans = []
	for i in range(len(a[0])):
		cur = []
		for j in range(len(a)):
			cur.append(a[j][i])
		ans.append(cur)
	return ans