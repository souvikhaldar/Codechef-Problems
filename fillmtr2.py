for i in range(int(input())):
    n,q=map(int,input().split())
    a=[]
    b=[]
    c={}
    e=[]
    flag=0
    for j in range(q):
        b=list(map(int,input().split()))
        a.append([b[0],b[1],b[2]])
    for k in a:
        c[str([k[0],k[1]])]=str(k[2])
    for j in c.keys():
        if j[1]==j[4]:
            if c[j]!=0:
                flag=1

        for k in c.keys():
            print(c[j],c[k])
            if c[j]==c[k]:
                if j[1]==c[1]:
                    if j[4]!=c[4]:
                        flag=1
                        break
                elif j[4]==c[4]:
                    if j[1]!=c[1]:
                        flag=1
                        break
                elif j[1]==c[4]:
                    if j[4]!=c[1]:
                        flag=1
                        break
                elif j[4]==c[1]:
                    if j[1]!=c[4]:
                        flag=1
                        break

    for l in a:
        e.append([l[0],l[1]])
    for m in e:
        print(m)
