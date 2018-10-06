for i in range(int(input())):
    b=[]
    c=[]
    d=[]
    n,m=map(int,input().split())
    a=[0 for x in range(n)]
    for j in range(m):
        t,l,r=map(int,input().split())
        b.append([t,l,r])
    for k in b:
        if k[0]==1:
            c.append([k[1],k[2],1])
        else:
            d.append([k[1],k[2]])
    for l in d:
        for m in range(l[0],l[1]+1):
            print(c[m][2])
    print(c)
