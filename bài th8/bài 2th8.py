print('Trần Văn Tú MSV 235752021610056')
import turtle

# Tạo đối tượng turtle
star = turtle.Turtle()

# Cài đặt tốc độ vẽ
star.speed(2)  # Tốc độ từ 1 (chậm) đến 10 (nhanh)

# Cài đặt màu sắc cho ngôi sao
star.color("blue")  # Đặt màu vẽ là xanh dương

# Vẽ ngôi sao 5 cánh
for _ in range(5):
    star.forward(100)  # Di chuyển về phía trước 100 đơn vị
    star.right(144)     # Quay 144 độ (để tạo góc giữa các cạnh ngôi sao)

# Ẩn bút vẽ (turtle)
star.hideturtle()

# Giữ cửa sổ đồ họa mở
turtle.done()
