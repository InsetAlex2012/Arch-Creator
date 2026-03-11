import numpy as np

def create_arch(pen, length, spacing):
    width = length
    pen.clear()

    for height in np.arange(0 - length, length + spacing, spacing):
        pen.penup()
        pen.goto(width, 0 - length)
        pen.pendown()
        pen.goto(0 - length, height)

        width -= spacing

if __name__ == "__main__": print("\033[31mThis is the arch library, please run the \"arch_creator\" program instead.\033[0m")