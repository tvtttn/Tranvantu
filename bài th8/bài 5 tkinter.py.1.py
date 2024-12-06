print('Trần Văn Tú MSV 235752021610056')
import tkinter as tk

# Callback function to display the selected choice
def ShowChoice():
    print(f"Selected language: {v.get()}")

# Create the main window
root = tk.Tk()
root.title("Indicator Example")

# Define choices
languages = ["Python", "JavaScript", "C++", "Java"]
v = tk.StringVar()  # Variable to store the selected value
v.set(languages[0])  # Set the default value

# Create indicator-style radio buttons
for language in languages:
    tk.Radiobutton(
        root,
        text=language,       # Button label
        indicatoron=0,       # Turn it into a button
        width=20,            # Set button width
        padx=20,             # Add padding
        variable=v,          # Use the shared variable
        command=ShowChoice,  # Function to call on click
        value=language       # Unique value for each button
    ).pack(anchor=tk.W)

# Run the GUI event loop
root.mainloop()
