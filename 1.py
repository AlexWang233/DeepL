def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	ans = []
	for i in a:
		cur = 0
		for j in range(len(i)):
			cur += (i[j] * b[j])
		ans.append(cur)
	return ans