# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:09:03 2024

@author: anitha
"""

import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result) + " ")
    except Exception as e:
        result_label.config(text="Error: " + str(e) + " ")

# Function to add a character to the entry field
def add_character(character):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + character)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget for user input
entry = tk.Entry(window, width=35, font=("Helvetica", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons for numbers
number_buttons = []
for i in range(9):
    button = tk.Button(window, text=str(i+1), command=lambda i=i: add_character(str(i+1)))
    button.grid(row=1+(i//3), column=i%3, padx=5, pady=5)
    button.config(width=8, height=3)  # Adjust button size
    number_buttons.append(button)

# Create the button for number 0
button_zero = tk.Button(window, text="0", command=lambda: add_character("0"))
button_zero.grid(row=4, column=1, padx=5, pady=5)
button_zero.config(width=8, height=3)  # Adjust button size

# Create the operator buttons
operator_buttons = ["+", "-", "*", "/", "%", "**"]
row = 1
col = 3
for operator in operator_buttons:
    button = tk.Button(window, text=operator, command=lambda operator=operator: add_character(operator))
    button.grid(row=row, column=col, padx=5, pady=5)
    button.config(width=8, height=3)  # Adjust button size
    row += 1

# Create additional operator buttons
button_dot = tk.Button(window, text=".", command=lambda: add_character("."))
button_dot.grid(row=4, column=0, padx=5, pady=5)
button_dot.config(width=8, height=3)  # Adjust button size

button_clear = tk.Button(window, text="C", command=lambda: entry.delete(0, tk.END))
button_clear.grid(row=4, column=2, padx=5, pady=5)
button_clear.config(width=8, height=3)  # Adjust button size

button_open_paren = tk.Button(window, text="(", command=lambda: add_character("("))
button_open_paren.grid(row=5, column=0, padx=5, pady=5)
button_open_paren.config(width=8, height=3)  # Adjust button size

button_close_paren = tk.Button(window, text=")", command=lambda: add_character(")"))
button_close_paren.grid(row=5, column=1, padx=5, pady=5)
button_close_paren.config(width=8, height=3)  # Adjust button size

button_equal = tk.Button(window, text="=", command=evaluate_expression)
button_equal.grid(row=5, column=2, padx=5, pady=5, rowspan=2)
button_equal.config(width=8, height=8)  # Adjust button size

# Create a label to display the result
result_label = tk.Label(window, text="Result:")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# Start the main event loop
window.mainloop()