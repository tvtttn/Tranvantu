input('Bùi Thế Tùng MSV 235752021610074')
import math
def calculate_distance(movements):
    #khởi tạo vị trí ban đầu
    x,y =0,0
    #duyệt qua các bước di chuyển
    for movement in movements:
        direction,step= movement.split()
        steps= int(steps)
        if direction =="UP":
            y +=steps
        elif direction =="DOWN":
            y -=steps
        elif direction =="LEFT":
            x -=steps
        elif direction == "RIGHT":
             x += steps
    # Tính khoảng cách từ vị trí hiện tại đến (0, 0)
             distance = math.sqrt(x**2 + y**2)
    # Làm tròn khoảng cách và chuyển đổi thành số nguyên
    return round(distance)
    # Nhập dữ liệu từ người dùng
    movements = []
    print("Nhập các bước di chuyển (nhập 'STOP' để kết thúc):")
while True:
    move = input()
    if move.strip().upper() == 'STOP':
        break
    movements.append(move)

# Tính và in ra khoảng cách
distance = calculate_distance(movements)
print(f"Khoảng cách từ vị trí hiện tại đến vị trí đầu tiên là: {distance}")
