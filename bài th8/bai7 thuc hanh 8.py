print('Trần Văn Tú MSV 235752021610056')
import tkinter as tk
import random
time_left = 120
score = 0
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Brown", "Pink", "White", "Black"]
def start_game(event=None):
    global time_left, score
    if time_left == 120:
        score = 0
        time_left = 120
        score_label.config(text=f"Điểm: {score}")
        time_label.config(text=f"Thời gian: {time_left}s")
        countdown()
        next_color()
def next_color():
    if time_left > 0:
        color_entry.focus_set()
        random.shuffle(colors)
        color_label.config(fg=colors[1].lower(), text=colors[0])  # Văn bản và màu chữ
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Thời gian: {time_left}s")
        window.after(1000, countdown)  # Lặp lại sau 1 giây
    else:
        color_label.config(text="Hết giờ!", fg="black")
        color_entry.config(state=tk.DISABLED)
def check_answer(event=None):
    global score
    if time_left > 0:
        if color_entry.get().strip().lower() == colors[1].lower():
            score += 2
        else:
            score -= 1
        score_label.config(text=f"Điểm: {score}")
        color_entry.delete(0, tk.END)
        next_color()
window = tk.Tk()
window.title("Game học màu sắc tiếng Anh")
window.geometry("400x300")
instructions = tk.Label(window, text="Nhập tên màu hiển thị, không phải màu chữ!", font=("Arial", 12))
instructions.pack(pady=10)
time_label = tk.Label(window, text=f"Thời gian: {time_left}s", font=("Arial", 14), fg="red")
time_label.pack()
score_label = tk.Label(window, text=f"Điểm: {score}", font=("Arial", 14), fg="blue")
score_label.pack()
color_label = tk.Label(window, font=("Arial", 40))
color_label.pack(pady=20)
color_entry = tk.Entry(window, font=("Arial", 14))
color_entry.pack()
color_entry.bind("<Return>", check_answer)
start_button = tk.Button(window, text="Bắt đầu", font=("Arial", 14), command=start_game)
start_button.pack(pady=10)
window.mainloop()
