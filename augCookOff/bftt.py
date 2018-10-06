def check(a):
    a = str(a)
    count = 0
    for i in a:
        if i == '3':
            count +=1
    if count >= 3:
        return True
    return False
a = int(input())
while a > 0:
    b = int(input())
    c = b + 1
    while c > b:
        if check(c):
            print(c)
            break
        c +=1
    a -= 1