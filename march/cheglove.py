import sys
for i in range(int(input())):
    front=1
    back=1
    both=1
    none=1
    a=input()
    b = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))
    for j in range(len(b)):
        if b[j] > c[j]:
            front = 0
            break
    for j in range(len(b)):
        if b[j] > c[len(b)-j-1]:
            back = 0
            break


    if front==1 and back==1:
        print("both")

    elif front==0 and back==0:
        print("none")

    elif front==1:
        print("front")
    elif back == 1:
        print("back")
