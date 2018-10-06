for i in range(int(input())):
    flag=0
    a,b,c,d = map(int,input().split())
    if a==b==c==d:
        flag=1
    elif a==b and c==d or a==c and b==d or a==d and b==c:
        flag=1
    if flag==1:
        print("YES")
    else:
        print("NO")
