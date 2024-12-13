print('Trần Văn Tú MSV 235752021610056')
import turtle

# Tạo một đối tượng turtle
pen = turtle.Turtle()

# Cài đặt tốc độ vẽ
pen.speed(2)  # 1 - chậm nhất, 10 - nhanh nhất, 0 - nhanh vô cùng

# Vẽ hình vuông
for _ in range(4):
    pen.forward(100)  # Di chuyển turtle 100 bước về phía trước
    pen.left(90)      # Quay turtle 90 độ sang trái

# Ẩn con turtle (bút vẽ) sau khi hoàn thành vẽ
pen.hideturtle()

# Giữ cửa sổ đồ họa mở
turtle.done()
