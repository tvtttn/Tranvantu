print('Trần Văn Tú MSV 235752021610056')
# Chương trình chính

# Nhập danh sách các phần tử từ bàn phím
n = int(input("Nhập số lượng phần tử trong danh sách: "))
lst = []

for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(element)

# Sắp xếp danh sách (vì tìm kiếm nhị phân chỉ hoạt động với danh sách đã sắp xếp)
lst.sort()

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Nhập module binary_search để sử dụng hàm tìm kiếm
import binary_search

# Sử dụng hàm binary_search để tìm phần tử
found = binary_search.binary_search(lst, value)

# In kết quả
if found:
    print(f"Phần tử {value} có trong danh sách.")
else:
    print(f"Phần tử {value} không có trong danh sách.")
