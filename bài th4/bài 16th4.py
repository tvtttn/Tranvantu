print('Trần Văn Tú MSV 235752021610056')
# Bước 1: Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi các số nhị phân, mỗi số cách nhau bởi dấu phẩy: ")

# Bước 2: Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# Bước 3: In ra các số nhị phân
print("Các số nhị phân bạn đã nhập:")
for binary in binary_numbers:
    print(binary)
