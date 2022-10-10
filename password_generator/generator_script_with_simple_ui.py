## This is going to use the same code, but with a simple UI

import random   # Import random module

from tkinter import *   # Import tkinter module

# Create a window

window = Tk()

# Create a label

label = Label(window, text="Password Generator")

# Create a button

button = Button(window, text="Generate Password")

# Create a text box

textbox = Text(window, height=1, width=16)

# Create a function to generate a password

def password_generator():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,./<>?|"
    all = lower_case + upper_case + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    textbox.insert(END, password)

# Create a function to clear the text box

def clear_textbox():
    textbox.delete(1.0, END)

# Create a function to copy the password to the clipboard

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(textbox.get(1.0, END))

# Create a function to quit the program

def destroy_program():
    window.destroy()