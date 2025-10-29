import tkinter as tk

# Global expression variable
expression = ""

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except Exception:
        equation.set("Error")
        expression = ""

# Function to clear expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to handle keyboard input
def key_event(event):
    key = event.char
    if key in "0123456789+-*/.":
        press(key)
    elif key == "\r":  # Enter key
        equalpress()
    elif key == "\x08":  # Backspace
        global expression
        expression = expression[:-1]
        equation.set(expression)

# Main GUI setup
def create_calculator():
    global equation
    root = tk.Tk()
    root.title("Polished Calculator")
    root.configure(bg="#f0f0f0")
    root.geometry("300x400")
    root.resizable(False, False)

    equation = tk.StringVar()

    entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief="ridge", justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
    entry.bind("<Key>", key_event)

    # Button layout
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("Clear", 5, 0, 4)
    ]

    for btn in buttons:
        text, row, col = btn[0], btn[1], btn[2]
        colspan = btn[3] if len(btn) == 4 else 1
        action = equalpress if text == "=" else clear if text == "Clear" else lambda x=text: press(x)
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="#d3d3d3", fg="black", command=action)\
            .grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

    # Make grid cells expand
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

    root.mainloop()

# Run the calculator
if __name__ == "__main__":
    create_calculator()
