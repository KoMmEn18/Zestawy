import time

def rec_p(i, j):
    if(i == 0 and j == 0):
        return 0.5
    if(j == 0):
        return 0
    if(i == 0):
        return 1.0
    
    return 0.5 * (rec_p(i-1, j) + rec_p(i, j-1))

def dyn_p(i, j):
    rows = i+1
    columns = j+1
    P = [ [None]*columns for n in range(rows)]
    P[0][0] = 0.5
    for n in range(1,rows):
        P[n][0] = 0.0
    for n in range(1,columns):
        P[0][n] = 1.0

    for m in range (1,rows):
        for n in range (1,columns):
            P[m][n] = 0.5 * (P[m-1][n] + P[m][n-1])
            
    return P[i][j]


if __name__ == "__main__":
    print(rec_p(3, 4))
    print(dyn_p(3, 4))

    print(rec_p(10, 5))
    print(dyn_p(10, 5))

    rec_start = time.time()
    for i in range(13):
        for j in range(13):
            rec_p(i, j)
    print("Recursive time: ", time.time() - rec_start)

    dyn_start = time.time()
    for i in range(13):
        for j in range(13):
            dyn_p(i, j)
    print("Dynamic time: ", time.time() - dyn_start)