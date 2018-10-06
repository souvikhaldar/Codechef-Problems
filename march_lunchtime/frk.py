i=int(input())
l=[]
flag=0
for j in range(i):
	a=input()
	l.append(a)
for k in l:
	if 'ch' in k or 'che' in k or 'chef' in k or 'he' in k or 'ef' in k or 'hef' in k:
		flag+=1
print(flag)
