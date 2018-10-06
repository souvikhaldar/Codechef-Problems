for i in range(int(input())):
    x,y,k,n = map(int,input().split())
    p = []
    q = []
    for j in range(n):
        a,b = map(int,input().split())
        p.append(a)
        q.append(b)
    req = x - y
    flag = 0
    for l in range(n):
        if req <= p[l]:
            if k >= q[l]:
                flag = 1
    if flag == 1:
        print("LuckyChef")
    else:
        print("UnluckyChef")
