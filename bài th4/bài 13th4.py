print('Trần Văn Tú MSV 235752021610056')
ds = ['123', '456', '789', 'abc', 'xyz']  # Ví dụ danh sách

# Tìm vị trí của phần tử 'abc'
try:
    index_abc = ds.index('abc')
    print("Vị trí của chuỗi 'abc' là:", index_abc)
except ValueError:
    print("Phần tử 'abc' không có trong danh sách.")
