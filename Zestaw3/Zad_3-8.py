def find_and_print_instersection_of_elements(first_sequence, second_sequence):
    print(set(first_sequence).intersection(second_sequence))

def find_and_print_union_of_elements(first_sequence, second_sequence):
    print(set(first_sequence).union(second_sequence))

if __name__ == "__main__":
    find_and_print_instersection_of_elements('aasdf123', '2assc2')
    find_and_print_union_of_elements('aasdf123', '2assc2')