for i in range(int(input())):
	c=0
	h=0
	n,p=map(int,input().split())
	l=list(map(int,input().strip().split()))
	for j in l:
		if int(j)>=(p//2):
			c+=1
		if int(j)<=(p//10):
			h+=1
	#print("Number of hard",h)
	#print("Number of cakewalk",c)
	if c==1 and h==2:
		print('yes')
	else:
		print('no')
			
