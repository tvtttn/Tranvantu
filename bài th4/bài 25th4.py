print('Trần Văn Tú MSV 235752021610056')
def filter_odd_numbers():
    # Nhập chuỗi các số từ người dùng, cách nhau bằng dấu phẩy
    input_data = input("Nhập danh sách các số (cách nhau bằng dấu phẩy): ")
    
    # Chuyển chuỗi thành danh sách các số nguyên
    numbers = [int(num.strip()) for num in input_data.split(',')]
    
    # Lọc các số lẻ
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # In kết quả dưới dạng chuỗi phân tách bằng dấu phẩy
    print(",".join(map(str, odd_numbers)))

# Gọi hàm
filter_odd_numbers()
