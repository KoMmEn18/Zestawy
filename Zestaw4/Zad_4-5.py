def iterative_reverse(L, left, right):
    if(right >= len(L)): return
    if(left < right):
        list_segment = L[left:right+1]
        done_segment = []
        for item in list_segment[::-1]:
            done_segment.append(item)
        
        L[left:right+1] = done_segment

def recursive_reverse(L, left, right):
    if(right >= len(L)): return
    if(left < right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        recursive_reverse(L, left + 1, right-1)


if __name__ == "__main__":
    L = list(range(10))
    iterative_reverse(L, 2, 6)
    print(L)
    L = list(range(10))
    recursive_reverse(L, 2, 8)
    print(L)