print('Trần Văn Tú MSV 235752021610056')
def check_divisible_by_5(binary_numbers):
    result = []  # Danh sách chứa các số nhị phân chia hết cho 5
    
    # Duyệt qua từng số nhị phân
    for bin_num in binary_numbers.split(','):
        # Chuyển đổi số nhị phân sang số thập phân
        decimal_value = int(bin_num, 2)
        
        # Kiểm tra xem số thập phân có chia hết cho 5 không
        if decimal_value % 5 == 0:
            result.append(bin_num)  # Nếu chia hết, thêm vào kết quả
    
    # In ra kết quả, các số nhị phân chia hết cho 5 được phân tách bằng dấu phẩy
    print(" ".join(result))

# Nhập chuỗi các số nhị phân phân tách bằng dấu phẩy
input_data = input("Nhập chuỗi các số nhị phân 4 chữ số (phân tách bởi dấu phẩy): ")

# Gọi hàm để kiểm tra và in kết quả
check_divisible_by_5(input_data)
