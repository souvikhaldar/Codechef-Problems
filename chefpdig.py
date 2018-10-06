import itertools

for i in range(int(input())):
    flag=0
    f=[]
    g=[]
    a=input()
    b=list(a)
    c=list(itertools.permutations(b,2))
    for j in c:
        d=''.join(map(str,j))
        e=int(d)
        if e not in f and e>=65 and e<=90:
            f.append(e)
        #print(f)
    f.sort()
    for k in range(len(f)):
        if f[k]>=65 and f[k]<=90:
            flag=1
            g.append(chr(f[k]))
    if flag==0:
        print()
    else:
        h=''.join(map(str,g))
        #print(type(h))
        print(h)
        #e=int()
        #e.append()
        #print(chr(int(d)))
