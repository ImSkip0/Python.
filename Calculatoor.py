import tkinter as tk

# --- Functions ---
def button_click(item):
    """Handles number and operator button clicks"""
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    """Clears the display"""
    display_var.set("")

def button_equal():
    """Calculates the expression"""
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except ZeroDivisionError:
        display_var.set("Error: Div by 0")
    except Exception:
        display_var.set("Syntax Error")

# --- 1. Main Window Setup ---
root = tk.Tk()
root.title("My Python Calculator")
root.geometry("360x420")
root.resizable(0, 0)
root.configure(bg="#f0f0f0")

display_var = tk.StringVar()

# --- 2. Display Screen ---
display = tk.Entry(
    root,
    textvariable=display_var,
    font=('Helvetica', 20, 'bold'),
    bg="#ffffff",
    bd=5,
    justify="right"
)

display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=15, padx=10)

# --- 3. Button Layout ---
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('C',4,0), ('0',4,1), ('=',4,2), ('+',4,3)
]

# --- 4. Create Buttons ---
for (text, row, col) in buttons:

    if text == '=':
        btn = tk.Button(root, text=text, font=('Helvetica',16,'bold'),
                        command=button_equal,
                        bg="#4CAF50", fg="white", height=2, width=5)

    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Helvetica',16,'bold'),
                        command=button_clear,
                        bg="#f44336", fg="white", height=2, width=5)

    else:
        btn = tk.Button(root, text=text, font=('Helvetica',16,'bold'),
                        command=lambda t=text: button_click(t),
                        height=2, width=5)

    btn.grid(row=row, column=col, padx=5, pady=5)

# --- 5. Run Application ---
root.mainloop()