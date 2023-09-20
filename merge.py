l_index = r_index = 0

def merge(left, right):
    S = []
    l_index = r_index = 0
    while (l_index < len(left) and r_index < len(right)):
        if (left[l_index] < right[r_index]):
            S.apppend(left[l_index])
            l_index += 1
        else:
            S.append(right[r_index])
            r_index += 1
            
    if (l_index < len(left)):
        S = S + left[l_index:len(left)]
    else:
        S = S +right[r_index:len(right)]
                