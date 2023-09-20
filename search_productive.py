def seq_search(n,S,x):
    location = 1
    while (location <= n and S[location] != s):
        location += 1
    if (location > n):
        location = 0
    return location