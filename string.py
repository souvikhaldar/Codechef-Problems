for i in range(int(input())):
	a=input()
	b={}
	count=0
	c=list(a)
	d={}
	flag=0
	for j in a:
		if j not in b.keys():
			b[j]=0
	for k in b.keys():
		for l in a:
			if k==l:
				b[k]+=1
	for m in b.values():
		if m>=2:
			count+=1
	if count>=2:
		for n in b.keys():
			if b[n]>=2:
				d[n]=[]
				while n in c:
					d[n].append(c.index(n))
					c[c.index(n)]='xyz'
		for o in d.keys():
			for p in d.keys():
				if o!=p:
					if d[o][0]<d[p][0]:
						if d[o][1]>d[p][1]:
							flag=1
					else:
						if d[o][1]<d[p][1]:
							flag=1
		if flag==0:
			print('yes')
		else:
			print('no')
	else:
		print('no')
