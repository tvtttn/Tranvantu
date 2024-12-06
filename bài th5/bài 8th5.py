print('Trần Văn Tú MSV 235752021610056')
# Chương trình chính

# Nhập danh sách các phần tử
n = int(input("Nhập số lượng phần tử trong danh sách: "))
dlist = []

for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(element)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Nhập module sequential_search để sử dụng hàm tìm kiếm
import sequential_search

# Sử dụng hàm Sequential_Search để tìm phần tử
found, index = sequential_search.Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy tại vị trí {index}.")
else:
    print(f"Phần tử {item} không có trong danh sách.")
