import random
import math

def generate_random_list(n):
    random_list = list(range(0, n))
    random.shuffle(random_list)

    return random_list

def generate_almost_sorted_list(n):
    random_list = list(range(0, n))
    numb_of_indexes = n//5
    for i in range(numb_of_indexes):
        rand_index_1 = random.randint(0,n-1)
        rand_index_2 = random.randint(0,n-1)
        random_list[rand_index_1], random_list[rand_index_2] = random_list[rand_index_2], random_list[rand_index_1]
    
    return random_list

def generate_almost_sorted_reversed_list(n):
    reverse_random_list = generate_almost_sorted_list(n)
    reverse_random_list.reverse()

    return reverse_random_list

def generate_random_list_with_gauss_distribution(n):
    random_list = []
    for i in range(n):
        random_list.append(random.gauss(0.0, 1.0))
    
    return random_list

def generate_random_list_with_duplicate_values(n):
    k = math.ceil(math.sqrt(n))
    random_list = []
    for i in range(n):
        random_list.append(random.randint(0, k))

    return random_list


if __name__ == "__main__":
    print(generate_random_list(20))
    print(generate_almost_sorted_list(20))
    print(generate_almost_sorted_reversed_list(20))
    print(generate_random_list_with_gauss_distribution(5))
    print(generate_random_list_with_duplicate_values(20))