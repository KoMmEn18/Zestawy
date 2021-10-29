def construct_and_draw_recrangle(width, height):
    width += 1
    rectangle = ""
    for j in range(0, height):
        rectangle += "---".join("+" for i in range(0, width))
        rectangle += "\n"
        rectangle += "   ".join("|" for i in range(0, width))
        rectangle += "\n"
    
    rectangle += "---".join("+" for i in range(0, width))
    print(rectangle)

if __name__ == "__main__":
    construct_and_draw_recrangle(4, 2)
    construct_and_draw_recrangle(8, 3)
    construct_and_draw_recrangle(5, 5)