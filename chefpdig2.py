for i in range(int(input())):
    c=[]
    d=[]
    e=[]
    a=input()
    flag=0
    for j in a:
            c.append(j)
    #print(c)
    f=c[:]
    for k in range(65,91):
        f=c[:]
        d=[]
        if str(k)[0] in f and str(k)[0]>='6' and str(k)[0]<='9':
            d.append(str(k)[0])
            f.remove(str(k)[0])
        if str(k)[1] in f:
            d.append(str(k)[1])
            f.remove(str(k)[1])
        if ''.join(map(str,d))>='65' and ''.join(map(str,d))<='90':
            e.append(chr(int((''.join(map(str,d))))))
            h=(''.join(map(str,e)))
            flag=1
    #print(type(h))
    if flag==0:
        pass
    else:
        print(h,end='')
        print(type(h))

    print()
