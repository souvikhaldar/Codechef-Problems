for i in range(int(input())):
	l=[]
	a=int(input())
	for j in range(a):
		if j==0:
			l.append(2)
		elif j<l[-1]:
			l.append(j)
		elif j>l[-1] and j+2<=a:
			l.append(j+2)
		else:
			l.append(j+1)
			(l[j-1],l[j])=(l[j],l[j-1])
	for k in range(len(l)):
		if k==len(l)-1:
			print(l[k])
		else:
			print(l[k],end=' ')
