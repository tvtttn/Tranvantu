input('Trần Văn Tú MSV 235752021610056')
# Nhập chuỗi từ bàn phím
input_string = input('Nhập chuỗi: ')

# Loại bỏ các chữ số
output_string = ''.join(ch for ch in input_string if not ch.isdigit())

# In ra chuỗi mới
print('Chuỗi sau khi loại bỏ chữ số:', output_string)
