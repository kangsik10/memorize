def recursive_binary_search(S, low, high, x):
    mid = (low + high) // 2
    if (x == S[mid]):
        return mid
    elif (x < S[mid]):
        return recursive_binary_search(S, low, mid-1, x)
    else:
        return recursive_binary_search(S, mid+1, high, x)
S = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45, 47]
x = 18
location = recursive_binary_search(S, 0, len(S), x)
print('S =', S)
print('x =', x)
print('location =', location)    
