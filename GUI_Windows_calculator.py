"""Python GUI simple calculator.
using Python version 3.12.0
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

import tkinter as tk

def main():
    """
    main function for interacting with the user
    """
    root = tk.Tk()
    # Create the main window

    root.title("Calculator")
    # set a window title

    root.configure(background = "grey")

    root.geometry("390x420")
    # set the initial screen size

    root.resizable(width = False, height = False)
    # lock screen size

    global entry 
    entry = tk.Entry(root, font = ("Helvetica", 24), justify = tk.RIGHT)    
    entry.grid(row = 1, column = 0, columnspan = 4, padx = 12, pady = 10)
    # create the entry widget for displaying the input and result

    buttons = [
        "7", "8", "9", 
        "4", "5", "6",
        "1", "2", "3", 
        "-", "0", ".",
        "/", "*", "+",
        "C", "=", "<--"]
    # create buttons for the calculator

    row_num = 2
    col_num = 0

    for button_text in buttons:
        tk.Button(root, text = button_text ,font = ("Ariel",12,"bold"), bd=9, width = 8, height = 1 ,activebackground = "lightgrey", 
            activeforeground = "red", command = lambda text = button_text: on_click(text)).grid(row = row_num, column = col_num, padx = 12, pady = 6)
        col_num += 1
        if col_num > 2:
            col_num = 0
            row_num += 1
            
    root.mainloop()
    # start the main event loop


def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "<--":
        old_Entry = str(entry.get())
        new_Entry = old_Entry[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, new_Entry)
    else:
        entry.insert(tk.END, button_text)


if __name__ == '__main__':
    main()
    # run the main function after executing this file