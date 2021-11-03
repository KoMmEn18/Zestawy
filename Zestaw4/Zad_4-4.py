def fibonnaci(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b

    return a

if __name__ == "__main__":
    print(fibonnaci(0))
    print(fibonnaci(1))
    print(fibonnaci(2))
    print(fibonnaci(5))
    print(fibonnaci(10))
    print(fibonnaci(18))