# File: main.py

# Nhập module mymath với tên gọi thay thế (alias) mt
import mymath as mt  # Đặt tên alias là mt

# Dữ liệu mẫu
values = [2, 4, 6, 8, 10]

# In ra các bình phương của các giá trị
print('Squares:')
for v in values:
    print(mt.square(v))  # Sử dụng alias mt để gọi hàm square

# In ra các lập phương của các giá trị
print('Cubes:')
for v in values:
    print(mt.cube(v))  # Sử dụng alias mt để gọi hàm cube

# In ra giá trị trung bình
print('Average: ' + str(mt.average(values)))  # Sử dụng alias mt để gọi hàm average
