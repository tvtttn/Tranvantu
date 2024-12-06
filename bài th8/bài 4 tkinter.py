print('Trần Văn Tú MSV 235752021610056')
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Cấu hình cửa sổ
root.title("Cửa sổ đồ họa với Tkinter")  # Tiêu đề cửa sổ
root.geometry("400x300")                 # Kích thước cửa sổ (rộng x cao)

# Tạo nhãn hiển thị văn bản
label = tk.Label(root, text="Chào mừng bạn đến với Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Hiển thị nhãn với khoảng cách dọc

# Tạo nút bấm
button = tk.Button(root, text="Nhấn vào tôi", font=("Arial", 12), command=lambda: print("Nút đã được nhấn!"))
button.pack(pady=10)

# Chạy vòng lặp sự kiện chính
root.mainloop()
