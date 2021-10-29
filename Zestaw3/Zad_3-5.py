def construct_and_draw_measure(length):
    length += 1
    measure_up_part = "....".join("|" for i in range(0, length))
    measure_down_part = "".join("0" if i == 0 else f'{i:5}' for i in range(0, length))
    print (f'{measure_up_part}\n{measure_down_part}')

if __name__ == "__main__":
    construct_and_draw_measure(5)
    construct_and_draw_measure(10)
    construct_and_draw_measure(20)