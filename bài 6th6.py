print('Trần Văn Tú MSV 235752021610056')
class StringManipulator:
    def __init__(self):
        self.input_string = ""  # Thuộc tính lưu trữ chuỗi nhập vào

    # Phương thức để nhận chuỗi từ người dùng
    def get_String(self):
        self.input_string = input("Nhập một chuỗi: ")  # Nhập chuỗi từ bàn phím

    # Phương thức để in chuỗi đã nhập dưới dạng chữ in hoa
    def print_String(self):
        print(self.input_string.upper())  # In chuỗi với chữ in hoa

# Tạo đối tượng của class StringManipulator
string_obj = StringManipulator()

# Gọi phương thức get_String để nhập chuỗi từ người dùng
string_obj.get_String()

# Gọi phương thức print_String để in chuỗi đã nhập ở dạng in hoa
string_obj.print_String()
