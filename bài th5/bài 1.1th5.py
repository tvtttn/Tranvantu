print('Trần văn Tú MSV 235752021610056')
# File: main.py

# Nhập module mymath
import mymath  # Lưu ý là không cần viết đuôi .py

# Dữ liệu mẫu
values = [2, 4, 6, 8, 10]

# In ra các bình phương của các giá trị
print('Squares:')
for v in values:
    print(mymath.square(v))  # Gọi hàm square từ module mymath

# In ra các lập phương của các giá trị
print('Cubes:')
for v in values:
    print(mymath.cube(v))  # Gọi hàm cube từ module mymath

# In ra giá trị trung bình
print('Average: ' + str(mymath.average(values)))  # Gọi hàm average từ module mymath
