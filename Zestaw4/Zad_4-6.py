def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:  
            sum += item
    return sum

if __name__ == "__main__":
    sequence = [[],[4],(1,2),[3,4],(5,6,7), [[2,3], 3]]
    print(sum_seq(sequence))
    sequence = (1,[4,2],(1,2), (3,(1,2)), 7,[3,4],5)
    print(sum_seq(sequence))