print('Trần Văn Tú MSV 235752021610056')
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Lựa chọn ngôn ngữ lập trình yêu thích")

# Tạo biến lưu giá trị được chọn
v = tk.IntVar()
v.set(1)  # Giá trị mặc định (Python)

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị lựa chọn
def ShowChoice():
    chosen_language = next(lang for lang, val in languages if val == v.get())
    print(f"Ngôn ngữ bạn chọn: {chosen_language}")
    lbl_result.config(text=f"Bạn đã chọn: {chosen_language}")

# Tạo nhãn hướng dẫn
tk.Label(
    root,
    text="Chọn ngôn ngữ lập trình yêu thích:",
    font=("Arial", 12),
    justify=tk.LEFT,
    padx=20
).pack(anchor=tk.W)

# Tạo các Radio Button
for language, val in languages:
    tk.Radiobutton(
        root,
        text=language,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val,
        font=("Arial", 10)
    ).pack(anchor=tk.W)

# Thêm nhãn để hiển thị kết quả lựa chọn
lbl_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
lbl_result.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
