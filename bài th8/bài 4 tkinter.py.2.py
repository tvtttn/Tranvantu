print('Trần Văn Tú MSV 235752021610056')
from tkinter import *

# Tạo cửa sổ chính
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

# Tạo nhãn hiển thị
lbl = Label(window, text="Hello", font=("Arial", 14))
lbl.grid(column=0, row=0)

# Phương thức xử lý sự kiện nút bấm
def clicked():
    lbl.configure(text="Button was clicked !!")

# Tạo nút bấm
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

# Phương thức xử lý sự kiện phím bấm
def on_key_press(event):
    lbl.configure(text=f"Key '{event.char}' was pressed!")

# Gán sự kiện nhấn phím cho cửa sổ
window.bind("<Key>", on_key_press)

# Chạy vòng lặp chính
window.mainloop()
