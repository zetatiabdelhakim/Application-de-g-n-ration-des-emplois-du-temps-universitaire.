import tkinter as tk

def function_to_be_called():
    # code to be executed when the "Enter" key is pressed
    print("Enter key was pressed")

# create the root window
root = tk.Tk()

# create the text entry widget
entry = tk.Entry(root)

# bind the function to the "Return" key (which is the same as the "Enter" key)
entry.bind("<Return>", function_to_be_called)

# pack the widget into the window
entry.pack()

# run the main loop
root.mainloop()