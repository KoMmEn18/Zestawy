def factorial(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    
    return fact

if __name__ == "__main__":
    print(factorial(6))
    print(factorial(3))
    print(factorial(7))