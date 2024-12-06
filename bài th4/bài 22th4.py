print('Trần văn Tú MSV 235752021610056')
def find_even_digit_numbers(start, end):
    result = []
    even_digits = {'0', '2', '4', '6', '8'}  # Các chữ số chẵn
    
    # Duyệt qua các số trong đoạn [start, end]
    for num in range(start, end + 1):
        # Chuyển số thành chuỗi và kiểm tra xem tất cả các chữ số đều là số chẵn
        if all(digit in even_digits for digit in str(num)):
            result.append(str(num))  # Nếu đúng, thêm vào danh sách kết quả
    
    # In kết quả dưới dạng chuỗi phân tách bằng dấu phẩy
    print(",".join(result))

# Gọi hàm với đoạn [1000, 3000]
find_even_digit_numbers(1000, 3000)
