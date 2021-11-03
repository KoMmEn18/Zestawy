def flatten_seq (sequence):
    L = []
    if isinstance(sequence, (list, tuple)):
        [L.extend (flatten_seq (e)) for e in sequence]
    else:
        L.extend ([sequence])
    return L

if __name__ == "__main__":
    print(flatten_seq([[],[4],(1,2),[3,4],(5,6,7), [[2,(1,(((2))),3),3], 3]]))
    print(flatten_seq([1,(2,3),[],[4,(5,6,7)],8,[9]]))