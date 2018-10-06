for i in range(int(input())):
    count=0
    a=list(map(int,input().split()))
    for j in a:
        if j==1:
            count+=1
    if count==0:
        print("Beginner")
    if count==1:
        print("Junior Developer")
    if count==2:
        print("Middle Developer")
    if count==3:
        print("Senior Developer")
    if count==4:
        print("Hacker")
    if count==5:
        print("Jeff Dean")
