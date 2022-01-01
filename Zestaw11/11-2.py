import list_generator

global_counter = 0

def quicksort(L, left, right):
    if left >= right:
        return
    global global_counter    
    f = open("SortData/sort" + str(global_counter) + ".dat", "w")
    for i, val in enumerate(L):
        f.write(str(i) + " " + str(val) + "\n")
    f.close()
    global_counter += 1
    L[left], L[(left + right) // 2] = L[(left + right) // 2], L[left]
    pivot = left
    for i in range(left + 1, right + 1):
        if L[i] < L[left]:
            pivot += 1
            L[pivot], L[i] = L[i], L[pivot]
    L[left], L[pivot] = L[pivot], L[left]
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

if __name__ == "__main__":
    random_list = list_generator.generate_random_list(20)
    print(random_list)
    quicksort(random_list, 0, 19)
    print(random_list)