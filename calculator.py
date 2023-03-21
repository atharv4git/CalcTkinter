import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")

        self.equation = tk.StringVar()
        self.equation.set("")

        self.entry = tk.Entry(self.master, textvariable=self.equation, width=50)
        self.entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        buttons = [
            "sin", "cos", "tan", "log",
            "(", ")", "^", "sqrt",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "pi", "e", "abs", "!",
            "mod", "deg", "rad", "="
        ]

        r = 1
        c = 0
        for button in buttons:
            self.create_button(button, r, c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def create_button(self, text, row, column):
        button_width = 6
        button_height = 2

        if text == "C":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.clear())
        elif text == "=":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.calculate())
        elif text == "sin":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text("math.sin(math.radians("))
        elif text == "cos":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text("math.cos(math.radians("))
        elif text == "tan":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text("math.tan(math.radians("))
        elif text == "log":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text("math.log10("))
        elif text == "sqrt":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text("math.sqrt("))
        elif text == "pi":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text(str(math.pi)))
        elif text == "e":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text(str(math.e)))
        elif text == "abs":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                               command=lambda: self.append_text("abs("))
        elif text == "mod":
            button = tk.Button(self.master, text=text, width=button_width, height = button_height, command = lambda: self.append_text("%"))
        elif text == "deg":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                           command=lambda: self.append_text("deg("))
        elif text == "rad":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                           command=lambda: self.append_text("rad("))
        elif text == "!":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                           command=lambda: self.append_text("!"))
        elif text == "^":
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                           command=lambda: self.append_text("**"))
        else:
            button = tk.Button(self.master, text=text, width=button_width, height=button_height,
                           command=lambda text=text: self.append_text(text))
        button.grid(row=row, column=column, padx=2, pady=2)

    def append_text(self, text):
        self.equation.set(self.equation.get() + str(text))

    def clear(self):
        self.equation.set("")

    def calculate(self):
        try:
            # Convert 'deg' to 'math.degrees' and 'rad' to 'math.radians'
            expression = self.equation.get().replace('deg(', 'math.degrees(').replace('rad(', 'math.radians(')
            result = eval(expression)
            self.equation.set(result)
        except:
            self.equation.set("ERROR")

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
