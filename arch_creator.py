# https://github.com/TkinterEP/ttkthemes/tree/master/screenshots

import turtle, tkinter as tk, darkdetect
from ttkthemes import ThemedTk
from tkinter import ttk

# =================================================================

reset_animation = None

theme = darkdetect.theme()

# -----------------------------------------------------------------

def start_creation():
    global reset_animation

    if not length_entry.get() or not spacing_entry.get():
        if reset_animation:
            root.after_cancel(reset_animation)

        title_label.configure(text="Please fill in all fields!", bg="red", font=("Rubik Mono One", 16))
        reset_animation = root.after(1500, lambda: title_label.configure(text="Arch Creator!", bg="light blue", font=("Rubik Mono One", 30)))
        return

    if int(length_entry.get()) == 0 or int(spacing_entry.get()) == 0:
        if reset_animation:
            root.after_cancel(reset_animation)

        title_label.configure(text="Values can't be 0!", bg="red", font=("Rubik Mono One", 16))
        reset_animation = root.after(1500, lambda: title_label.configure(text="Arch Creator!", bg="light blue", font=("Rubik Mono One", 30)))

        return

    if not side_box.get():
        if reset_animation:
            root.after_cancel(reset_animation)
        title_label.configure(text="Please select a side!", bg="red", font=("Rubik Mono One", 16))
        reset_animation = root.after(1500, lambda: title_label.configure(text="Arch Creator!", bg="light blue", font=("Rubik Mono One", 30)))

        return

    if theme_box.get() == "Auto":
        if theme == "Light":
            turtle_root.bgcolor("white")
            pen.pencolor("black")
        else:
            turtle_root.bgcolor("black")
            pen.pencolor("white")

    elif theme_box.get() == "Dark":
        turtle_root.bgcolor("black")
        pen.pencolor("white")

    elif theme_box.get() == "Light":
        turtle_root.bgcolor("white")
        pen.pencolor("black")

    else:
        if reset_animation:
            root.after_cancel(reset_animation)
        title_label.configure(text="Please select a theme!", bg="red", font=("Rubik Mono One", 16))
        reset_animation = root.after(1500, lambda: title_label.configure(text="Arch Creator!", bg="light blue", font=("Rubik Mono One", 30)))

        return

    try:
        import arch_library as al

        turtle_root.getcanvas().winfo_toplevel().deiconify()

        create_button.configure(state="disabled")
        al.create_arch(pen, length=int(length_entry.get()), spacing=int(spacing_entry.get()), corner = side_box.get())
        create_button.configure(state="normal")

        if reset_animation:
            root.after_cancel(reset_animation)

        title_label.configure(text="Arch Completed!", bg="green", font=("Rubik Mono One", 20))
        reset_animation = root.after(2000, lambda: title_label.configure(text="Arch Creator!", bg="light blue", font=("Rubik Mono One", 30)))


    except ImportError:
        print("\033[31mLibrary not functioning correctly. Please check if the \"arch_library\" program is installed and in the same directory as the \"arch_creator\" program.\033[0m")
        exit()


    except tk.TclError:
        print("Program force closed.")
        exit()

# =================================================================

root = ThemedTk(theme = "breeze")

screen_width = 500
screen_height = 420

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

turtle_root.getcanvas().winfo_toplevel().withdraw()


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

def on_turtle_close():
    turtle.bye()
    if root.winfo_exists():
        create_button.configure(state="normal")
        root.destroy()
    print("Program force closed.")

def on_root_close():
    try:
        turtle.bye()
    except turtle.Terminator:
        pass
    root.destroy()
    print("Program force closed.")

root.protocol("WM_DELETE_WINDOW", on_root_close)
turtle_root.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_turtle_close)

# =================================================================

def only_numbers(char): return char.isdigit()
vcmd = (root.register(only_numbers), "%S")


button_style = ttk.Style()
button_style.configure("TButton", font = ("Rubik Mono One", 20))


root.option_add("*TCombobox*Listbox.font", ("Rubik Mono One", 15))

# -----------------------------------------------------------------

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

# -----------------------------------------------------------------

side_frame = tk.Frame(root)
side_frame.pack(pady = 5)


side_label = tk.Label(side_frame, text = "Side:", background = "light blue", font = ("Rubik Mono One", 15))
side_label.pack(side = tk.LEFT)

side_box = ttk.Combobox(side_frame, font = ("Rubik Mono One", 15), width = 12, state = "readonly")
side_box["values"] = ("Bottom left", "Bottom right", "Top left", "Top right")
side_box.current(0)
side_box.pack(padx = 30, side = tk.LEFT)

# -----------------------------------------------------------------

theme_frame = tk.Frame(root)
theme_frame.pack(pady = 5)


theme_label = tk.Label(theme_frame, text = "Theme:", background = "light blue", font = ("Rubik Mono One", 15))
theme_label.pack(side = tk.LEFT)

theme_box = ttk.Combobox(theme_frame, font = ("Rubik Mono One", 15), width = 12, state = "readonly")
theme_box["values"] = ("Auto", "Dark", "Light")
theme_box.current(0)
theme_box.pack(padx = 30, side = tk.LEFT)

# -----------------------------------------------------------------

create_button = ttk.Button(root, text = "Create!", style = "TButton", command = start_creation)
create_button.pack(pady = 20)

# =================================================================

root.mainloop()