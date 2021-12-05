import random
import math;

def calc_pi(n=100):
    hitCounter = 0
    random.seed(1)
    for i in range(n):
        x = random.random()
        y = random.random()
        if(y <= math.sqrt(1-math.pow(x,2))):
            hitCounter += 1

    print('Wartosc PI dla n = " + {} + ": " {}'.format(n, (hitCounter*4.0)/n))

if __name__ == "__main__":
    calc_pi(3)
    calc_pi(10)
    calc_pi(100)
    calc_pi(1000)
    calc_pi(10000)
    calc_pi(1000000)