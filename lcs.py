def lcs(A, B):
	m = len(A)
	n = len(B)
	opt = [[0 for row in range(m+1)] for col in range(n+1)]
	optshow = [[0 for row in range(m+1)] for col in range(n+1)]
	for j in range(m+1):
		opt[0][j] = 0

	for i in range(1, n+1):
		opt[i][0] = 0
		for j in range(1, m+1):
			if(A[j-1] == B[i-1]):
				opt[i][j] = opt[i-1][j-1] + 1
				optshow[i][j] = 's'
			elif(opt[i][j-1] >= opt[i-1][j]):
				opt[i][j] = opt[i][j-1]
				optshow[i][j] = '<'
			else:
				opt[i][j] = opt[i-1][j]
				optshow[i][j] = '^'

	# for i in opt:
	# 	print(i)
	# for i in optshow:
	# 	print(i)

	ans = ''
	count = 0
	i = n 
	j = m
	while i > 0 and j > 0:
		if(optshow[i][j] == 's'):
			ans = A[j-1] + ans
			count += 1
			i -=1
			j -=1
		elif optshow[i][j] == '^':
			i -= 1
		else:
			j -= 1

	print(count)
	print(ans)

ip = input()
ip = ip.split()
B = ip[0]
A = ip[1]

lcs(A, B)