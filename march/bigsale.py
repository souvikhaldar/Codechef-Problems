for i in range(int(input())):
    loss = 0
    for j in range(int(input())):
        a,b,c = map(int,input().strip().split())
        d = a - ((a * ((10000) - (c * c)))/10000)
        e = d * b
        loss = loss + e
    print(loss)
