import sys
for i in range(int(input())):
    flag=0
    b=[]
    l=[]
    d=[]
    e={}
    f=[]
    n,q=map(int,input().split())
    for j in range(q):
        l=list(map(int,input().split()))
        b.append(l)
        e[str([l[0],l[1]])]=str(l[2])
    for k in b:
        #print(k)
        if k[0]==k[1]:
            if k[2]!=0:
                #print('first wala')
                flag=1
                sys.exit()
        d.append([k[0],k[1]])
        #print(d)
        if [k[1],k[0]] in d:
            #print('fasa beta')
            if e[str([k[0],k[1]])]!=e[str([k[1],k[0]])]:
                flag=1
    for k in b:
        g=e[str([k[0],k[1]])]
        for n in b:
            if e[str([n[0],n[1]])]==g and str([k[0],k[1]])!=str([n[0],n[1]]):
                if k[0]==n[0] or k[0]==n[1] or k[1]==n[0] or k[1]==n[1]:
                    if k[0]!=n[0]:
                        if [k[0],n[0]] in d:
                            if e[str([k[0],n[0]])]!=0:
                                flag=1

                    elif k[0]!=n[1]:
                        if [k[0],n[1]] in d:
                            if e[str([k[0],n[1]])]!=0:
                                flag=1

                    elif k[1]!=n[0]:
                        if [k[1],n[0]] in d:
                            if e[str([k[1],n[0]])]!=0:
                                flag=1

                    else:
                        if [k[1],n[1]] in d:
                            if e[str([k[1],n[1]])]!=0:
                                flag=1

        f.append(g)


    if flag==0:
        print('yes')
    else:
        print('no')
