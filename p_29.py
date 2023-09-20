def recursive_binary_search(S, low, high, x):
    mid = (low + high) //2
    if (x == S[mid]):
        return mid
    elif (x < S[mid]):
        return recursive_binary_search(S, low, mid-1, x)
    else:
        return recursive_binary_search(S, mid+1, high, x)
    
(10, 1, 20, 2)