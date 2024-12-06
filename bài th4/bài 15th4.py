print('Trần Văn Tú MSV 235752021610056')
# Bước 1: Nhập chuỗi từ người dùng
input_string = input("Nhập các từ tiếng Anh (tách nhau bởi dấu cách): ")

# Bước 2: Tách chuỗi thành danh sách các từ
words = input_string.split()

# Bước 3: Sắp xếp các từ theo thứ tự từ điển
words.sort()

# Bước 4: In các từ đã sắp xếp
print("Các từ theo thứ tự từ điển:")
for word in words:
    print(word)
