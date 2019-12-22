t = int(input())
for i in range(t):
    inp = input()
    final = inp[:]
    steps = 0
    for i in range(len(inp)-3):
        inter = inp[i:i+4]
        if inter == "0101":
            inp = inp[:i+2] + inp[i+3:]
            steps += 1
        if inter == "1010":
            inp = inp[:i+1] + inp[i+2:]
            steps += 1

    print(steps)
