print('Bùi Thế Tùng MSV 235752021610074')
from tkinter import *

# Tạo cửa sổ chính
window = Tk()
window.title("Thay đổi màu nền và màu chữ")
window.geometry('350x200')

# Tạo nhãn hiển thị
lbl = Label(window, text="Nhấn nút để thay đổi màu", font=("Arial", 14))
lbl.pack(pady=10)

# Hàm xử lý khi nút được nhấn
def on_button_click():
    lbl.configure(text="Bạn đã nhấn nút!", fg="blue")

# Tạo Button với màu nền và màu chữ tùy chỉnh
btn = Button(window, text="Nhấn vào tôi", bg="green", fg="white", font=("Arial", 12), command=on_button_click)
btn.pack(pady=20)

# Chạy vòng lặp chính
window.mainloop()
