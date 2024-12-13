print('Trần Văn Tú MSV 235752021610056')
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Cấu hình cửa sổ
root.title("Thêm Button vào Window Form")
root.geometry("400x300")

# Tạo nhãn hiển thị
label = tk.Label(root, text="Chào mừng bạn đến với ứng dụng!", font=("Arial", 14))
label.pack(pady=20)

# Thêm Button vào cửa sổ
def on_button_click():
    label.config(text="Bạn đã nhấn nút!")  # Thay đổi nội dung nhãn khi bấm nút

button = tk.Button(root, text="Nhấn vào tôi", font=("Arial", 12), command=on_button_click)
button.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
