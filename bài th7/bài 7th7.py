print('Trần Văn Tú MSV 235752021610056')
# Đếm số dòng trong tệp văn bản

def count_lines(filename):
    try:
        # Mở tệp để đọc
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Đọc tất cả các dòng trong tệp
            return len(lines)  # Trả về số lượng dòng
    except FileNotFoundError:
        print(f"Tệp {filename} không tồn tại.")
        return 0
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return 0

# Nhập tên tệp
filename = input("Nhập tên tệp: ")

# Gọi hàm và in ra kết quả
line_count = count_lines(filename)
if line_count > 0:
    print(f"Số dòng trong tệp '{filename}' là: {line_count}")
