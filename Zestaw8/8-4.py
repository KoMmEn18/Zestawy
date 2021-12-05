import math

def heron(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
        if(a >= b + c):
            raise ValueError('Warunek trójkąta niespełniony')
    elif (b >= a) and (b >= c):
        largest = b
        if(b >= a + c):
            raise ValueError('Warunek trójkąta niespełniony')
    else:
        largest = c
        if(c >= a + b):
            raise ValueError('Warunek trójkąta niespełniony')
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print('Pole trojkata o bokach {}, {}, {} wynosi {}'.format(a, b, c, area))
    
if __name__ == "__main__":
    heron(6, 8, 10)
    heron(4, 5, 7)
    heron(7, 5, 10)
    heron(10, 10, 10)