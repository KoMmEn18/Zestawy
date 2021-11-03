def construct_and_draw_measure(length):
    length += 1
    measure_up_part = "....".join("|" for i in range(0, length))
    measure_down_part = "".join("0" if i == 0 else f'{i:5}' for i in range(0, length))

    return (f'{measure_up_part}\n{measure_down_part}')

def construct_and_draw_recrangle(width, height):
    width += 1
    rectangle = ""
    for j in range(0, height):
        rectangle += "---".join("+" for i in range(0, width))
        rectangle += "\n"
        rectangle += "   ".join("|" for i in range(0, width))
        rectangle += "\n"
    
    rectangle += "---".join("+" for i in range(0, width))
    
    return rectangle

if __name__ == "__main__":
    print(construct_and_draw_measure(12))
    print(construct_and_draw_recrangle(8, 3))