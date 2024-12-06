print('Trần Văn Tú MSV 235752021610056')
import numpy as np

# Dữ liệu đầu vào: Mảng có cấu trúc
data = np.array([('James', 5, 48.5),
                 ('Nail', 6, 52.5),
                 ('Paul', 5, 42.1),
                 ('Pit', 5, 40.11)],
                dtype=[('Name', 'U10'), ('Class', 'i4'), ('Height', 'f4')])

# Sắp xếp theo 'Class' (lớp), nếu lớp bằng nhau thì sắp xếp theo 'Height' (chiều cao)
sorted_data = np.sort(data, order=['Class', 'Height'])

# In kết quả
print(sorted_data)
