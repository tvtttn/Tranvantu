print('Trần Văn Tú MSV 235752021610056')
# Viết nội dung danh sách vào tệp

def write_list_to_file(filename, data_list):
    try:
        # Mở tệp để ghi (nếu tệp chưa tồn tại, Python sẽ tạo mới)
        with open(filename, 'w', encoding='utf-8') as file:
            # Duyệt qua từng phần tử trong danh sách và ghi vào tệp
            for item in data_list:
                file.write(str(item) + '\n')  # Ghi từng phần tử vào tệp và xuống dòng
        print(f"Nội dung danh sách đã được ghi vào tệp {filename}.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ về danh sách
my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Nhập tên tệp
filename = input("Nhập tên tệp: ")

# Ghi danh sách vào tệp
write_list_to_file(filename, my_list)
