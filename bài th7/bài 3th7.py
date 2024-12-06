print('Trần Văn Tú MSV 235752021610056')
def read_file(file_name):
    try:
        # Mở tệp ở chế độ đọc ('r')
        with open(file_name, 'r',encoding='utf-8') as file:
            # Đọc toàn bộ nội dung của tệp
            content = file.read()

        # In ra nội dung của tệp
        print('Nội dung tệp:')
        print(content)

    except FileNotFoundError:
        print(f"Tệp '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# Tên tệp cần đọc
file_name = 'D:/a.txt'

# Gọi hàm để đọc và in nội dung tệp
read_file(file_name)
