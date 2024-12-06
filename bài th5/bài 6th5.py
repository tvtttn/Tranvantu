print('Trần Văn Tú MSV 235752021610056')
# Chương trình chính

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập giá trị các phần tử của danh sách
lst = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(element)

# Nhập module list_utils để sử dụng các hàm
import list_utils

# Sắp xếp danh sách
sorted_lst = list_utils.sort_list(lst)

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = list_utils.find_max(lst)
min_value = list_utils.find_min(lst)

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất
max_index = list_utils.find_max_index(lst, max_value)
min_index = list_utils.find_min_index(lst, min_value)

# In kết quả
print(f"Danh sách sau khi sắp xếp: {sorted_lst}")
print(f"Phần tử lớn nhất: {max_value} ở vị trí {max_index}")
print(f"Phần tử nhỏ nhất: {min_value} ở vị trí {min_index}")
