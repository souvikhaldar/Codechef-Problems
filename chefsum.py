for i in range(int(input())):
	f=[]
	a=input()
	b=list(map(int,input().split()))
	c=sum(b)
	for j in b:
		f.append(c+j)
	d=min(f)
	for k in range(len(f)):
		if f[k]==d:
			print(k+1)
			break
