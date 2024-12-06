print('Trần Văn Tú MSV 235752021610056')
# Chương trình chính

# Nhập danh sách các phần tử từ bàn phím
n = int(input("Nhập số lượng phần tử trong danh sách: "))
nlist = []

for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(element)

# Nhập module bubble_sort để sử dụng hàm sắp xếp
import bubble_sort

# Sử dụng hàm bubbleSort để sắp xếp danh sách
sorted_list = bubble_sort.bubbleSort(nlist)

# In kết quả
print("Danh sách sau khi sắp xếp:", sorted_list)
