def find_sum_of_numbers_in_every_sequence(sequence_list):
    print([sum(sequence) for sequence in sequence_list])

if __name__ == "__main__":
    find_sum_of_numbers_in_every_sequence([[],[4],(1,2),[3,4],(5,6,7)])
    find_sum_of_numbers_in_every_sequence([[123,3],[2,0,2,-1],(3,-42),[1,4,76]])