print('Trần Văn Tú MSV 235752021610056')
class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Tách chuỗi thành các từ, đảo ngược danh sách các từ và nối lại thành chuỗi
        words = self.input_string.split()  # Tách chuỗi thành các từ
        reversed_words = ' '.join(reversed(words))  # Đảo ngược thứ tự các từ và nối lại
        return reversed_words


# Dữ liệu vào
input_string = 'hello .py'

# Khởi tạo đối tượng StringReverser
reverser = StringReverser(input_string)

# Lấy kết quả và in ra
result = reverser.reverse_words()
print(result)
