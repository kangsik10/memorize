def partition (S, low, high):
    if (low >= high):
        return
    pivotitem = S[low]
    left = low + 1
    right = high
    while (left < right):
        while (left < high and S[left] > pivotitem):
            left += 1
        while (S[right] > pivotitem):
            right -= 1
        if (left < right):
            S[left], S[right] = S[right], S[left]
    pivotpoint = right
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

def quicksort (S, low, high):
    if (high > low):
        pivotpoint = partition (S, low, high)
        quicksort (S, low, pivotpoint - 1)
        quicksort (S, pivotpoint + 1, high)
        
S = [61, 5, 37, 26, 1, 11, 59, 15, 48, 19]

print('Before:', S)
quicksort(S, 0, len(S) - 1)
print('After:', S)