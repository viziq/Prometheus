def saddle_point(matrix):
	xy=()
	spismin=[]
	spispos=[]
	x=0
	y=0
	num=0
	flag=False
	for i in range(len(matrix)):
		min=matrix[i][0]
		for j in range(len(matrix[i])):
			x=i
			if matrix[i][j]<min:
				x=i
				y=j
				min=matrix[i][j]
		xy=(x,y)
		spismin.append(min)
		spispos.append(xy)
	if len(matrix)==1:
		return (0,0)
	for l in range(len(spismin)):
		for k in range(len(matrix)):
			if spismin[l]>matrix[k][spispos[l][1]]:
				num=num+1
			if num==len(matrix)-1:
				if matrix[spispos[l][0]].count(spismin[l])==1:
					flag=True
					return spispos[l]
				else:
					flag=False
	if not flag:
		return False
print saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
print saddle_point([[1,2,3],[3,2,1]])
print saddle_point([[21]])
