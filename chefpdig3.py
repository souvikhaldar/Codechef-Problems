for i in range(int(input())):
    b=[]
    d=[]
    a=input()
    for j in range(65,91):
        c=list(a).copy()
        if str(j)[0] in c:
            c.remove(str(j)[0])
            if str(j)[1] in c:
                b.append(j)
    if b==[]:
        print()
    else:
        for k in b:
            d.append(chr(int(k)))
        f=''.join(d)
        print(f)
