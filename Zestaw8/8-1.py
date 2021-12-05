def solve1(a, b, c):
    if(a == 0):
        if(b == 0):
            if(c == 0):
                print('x oraz y należą do zbioru liczb rzeczywistych')
            else:
                print('Rownanie {} * x + {} * y + {} = 0 jest sprzeczne'.format(a, b, c))
        else:
            if(c == 0):
                print('x należy do zbioru liczb rzeczywistych, y = 0')
            else:
                print('x należy do zbioru liczb rzeczywistych, y = {}'.format(-c/b))
    else:
        if(b == 0):
            if(c == 0):
                print('x = 0, y należy do zbioru liczb rzeczywistych')
            else:
                print('x = {}, y należy do zbioru liczb rzeczywistych'.format(-c/a))
        else:
            if(c == 0):
                print('x należy do zbioru liczb rzeczywistych, y = {}*x'.format(-a/b))
            else:
                print('x należy do zbioru liczb rzeczywistych, y = {}*x + {}'.format(-a/b, -c/b))


if __name__ == "__main__":
    solve1(0, 0, 1)
    solve1(0, 0, 0)
    solve1(0, 1, 0)
    solve1(0, 1, 2)
    solve1(0, 1, 2)
    solve1(1, 0, 0)
    solve1(1, 0, 2)
    solve1(1, 2, 2)
    solve1(-1, 2, 0)
    solve1(1, -2, 0)