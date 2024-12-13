print('Trần Văn Tú MSV 235752021610056')
from tkinter import *

# Function for the "New" menu option
def NewFile():
    print("New File!")

# Function for the "About" menu option
def About():
    print("This is a simple example of a menu")

# Create the main application window
root = Tk()
root.title("Menu Example")  # Set the window title

# Create the main menu bar
menu = Menu(root)
root.config(menu=menu)  # Attach the menu bar to the window

# Create the "File" menu
filemenu = Menu(menu, tearoff=0)  # Disable default tear-off
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)  # Add "New" option
filemenu.add_separator()  # Add a separator
filemenu.add_command(label="Exit", command=root.quit)  # Add "Exit" option

# Create the "Help" menu
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)  # Add "About" option

# Run the application
mainloop()
