print('Trần Văn Tú MSV 235752021610056')
import numpy as np

# Tạo kiểu dữ liệu cấu trúc cho mảng
dtype = [('name', 'U50'), ('height', 'f4'), ('class', 'U20')]

# Dữ liệu của sinh viên
data = [
    ('Alice', 1.65, '10A'),
    ('Bob', 1.80, '10B'),
    ('Charlie', 1.70, '10C'),
    ('David', 1.75, '10A'),
    ('Eva', 1.60, '10B')
]

# Tạo mảng NumPy có kiểu dữ liệu cấu trúc
students = np.array(data, dtype=dtype)

# Sắp xếp mảng theo chiều cao (tăng dần)
sorted_students = np.sort(students, order='height')

# In kết quả
print("Danh sách sinh viên đã sắp xếp theo chiều cao:")
for student in sorted_students:
    print(f"Tên: {student['name']}, Chiều cao: {student['height']} m, Lớp: {student['class']}")
