# https://github.com/TkinterEP/ttkthemes/tree/master/screenshots

import turtle, tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk


def start_creation():
    if not length_entry.get() or not spacing_entry.get():
        title_label.configure(text = "Please fill in all fields", bg = "red", font = ("Rubik Mono One", 16))
        return

    try:
        import arch_library as al

        turtle_root.getcanvas().winfo_toplevel().deiconify()

        al.create_arch(pen, length = int(length_entry.get()), spacing = int(spacing_entry.get()))


    except ImportError:
        print(
            "\033[31mLibrary not functioning correctly. Please check if the \"arch_library\" program is installed and in the same directory as the \"arch_creator\" program.\033[0m")
        exit()

# =================================================================

root = ThemedTk(theme = "breeze")

screen_width = 500
screen_height = 320

screen_width_middle = int(root.winfo_screenwidth() / 2 - screen_width / 2)
screen_height_middle = int(root.winfo_screenheight() / 2 - screen_height / 2)

root.geometry(f"{screen_width}x{screen_height}+{screen_width_middle}+{screen_height_middle}")
root.title("Arch Creator! - Python Project")
root.configure(themebg="breeze")
root.resizable(False, False)

root.lift()
root.focus_force()

# =================================================================

turtle_root = turtle.Screen()
turtle_root.title("Arch Test")
turtle_root.setup(width=1.0, height=1.0)
turtle_root.bgcolor("black")

turtle_root.getcanvas().winfo_toplevel().withdraw()


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.pencolor("white")

def on_turtle_close():
    turtle.bye()
    root.destroy()
    print("Program force closed.")

turtle_root.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_turtle_close)

# =================================================================

def only_numbers(char): return char.isdigit()
vcmd = (root.register(only_numbers), "%S")

button_style = ttk.Style()
button_style.configure("TButton", font = ("Rubik Mono One", 20))


title_label = tk.Label(root, text = "Arch Creator!", background = "light blue", font = ("Rubik Mono One", 30))
title_label.pack(pady = 30)

# -----------------------------------------------------------------

length_frame = tk.Frame(root)
length_frame.pack(pady = 5)


length_label = tk.Label(length_frame, text = "Length:", background = "light blue", font = ("Rubik Mono One", 15))
length_label.pack(side = tk.LEFT)

length_entry = ttk.Entry(length_frame, validate = "key", validatecommand = vcmd, font = ("Rubik Mono One", 15), width = 10)
length_entry.pack(padx = 30, side = tk.LEFT)

# -----------------------------------------------------------------

spacing_frame = tk.Frame(root)
spacing_frame.pack(pady = 5)


spacing_label = tk.Label(spacing_frame, text = "Spacing:", background = "light blue", font = ("Rubik Mono One", 15))
spacing_label.pack(side = tk.LEFT)

spacing_entry = ttk.Entry(spacing_frame, validate = "key", validatecommand = vcmd, font = ("Rubik Mono One", 15), width = 10)
spacing_entry.pack(padx = 30, side = tk.LEFT)

create_button = ttk.Button(root, text = "Create!", style = "TButton", command = start_creation)
create_button.pack(pady = 20)

# =================================================================

root.mainloop()