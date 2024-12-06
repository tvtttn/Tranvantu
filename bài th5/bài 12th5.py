print('Trần Văn Tú MSV 235752021610056')
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sử dụng lexsort để sắp xếp theo chiều cao, nếu chiều cao giống nhau thì sắp xếp theo id sinh viên
# Hàm lexsort yêu cầu các mảng cần sắp xếp phải được truyền vào theo thứ tự ưu tiên (cột cuối cùng đến cột đầu tiên).
indices = np.lexsort((student_id, student_height))

# Sắp xếp dữ liệu theo chỉ số vừa tìm được
sorted_student_id = student_id[indices]
sorted_student_height = student_height[indices]

# In kết quả
print("Chỉ số:")
print(indices)
print("\nDữ liệu sắp xếp:")
for sid, height in zip(sorted_student_id, sorted_student_height):
    print(sid, height)
