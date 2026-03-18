import numpy as np

def create_arch(pen, length, spacing, corner):
    pen.clear()

    if corner == "Bottom left":
        width = length

        for height in np.arange(0 - length, length + spacing, spacing):
            pen.penup()
            pen.goto(width, 0 - length)
            pen.pendown()
            pen.goto(0 - length, height)

            width -= spacing

    elif corner == "Bottom right":
        width = 0 - length

        for height in np.arange(0 - length, length + spacing, spacing):
            pen.penup()
            pen.goto(width, 0 - length)
            pen.pendown()
            pen.goto(length, height)

            width += spacing

    elif corner == "Top left":
        width = length

        for height in np.arange(length, 0 - length - spacing, -spacing):
            pen.penup()
            pen.goto(width, length)
            pen.pendown()
            pen.goto(0 - length, height)

            width -= spacing

    elif corner == "Top right":
        width = 0 - length

        for height in np.arange(length, 0 - length - spacing, -spacing):
            pen.penup()
            pen.goto(width, length)
            pen.pendown()
            pen.goto(length, height)

            width += spacing


if __name__ == "__main__": print("\033[31mThis is the arch library, please run the \"arch_creator\" program instead.\033[0m")