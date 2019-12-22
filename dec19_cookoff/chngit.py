t = int(input())
for i in range(t):
    waste = input()
    inputs = list(map(int,input().split()))
    aux = inputs[:]
    # first calculate the frequency of each element in the list
    freq = {}
    for j in range(len(inputs)):
        if inputs[j] == 12345:
            continue
        val = inputs[j]
        freq[val] = 0
        for k in range(len(inputs)):
            if inputs[k] == val:
                freq[val] += 1
                inputs[k] = 12345
    # now find the element which occurs the most
    maxi = 0
    max_el = 0
    for k,v in freq.items():
        if v > maxi:
            maxi = v
            max_el = k
    # now calculate how many moves are required to make each element equal to max_el
    moves = 0
    for l in aux:
        if l != max_el:
            moves +=1
    print(moves)


    
