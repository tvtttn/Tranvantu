input('Trần văn Tú MSV 235752021610056')
# Nhập dãy các từ từ bàn phím
input_string = input('Nhập dãy các từ (cách nhau bằng khoảng trắng): ')

# Tách các từ trong chuỗi
words = input_string.split()

# Tìm độ dài lớn nhất của các từ
max_length = max(len(word) for word in words)

# Tìm các từ có độ dài bằng max_length
longest_words = [word for word in words if len(word) == max_length]

# In ra các từ dài nhất
print('Các từ dài nhất:', ', '.join(longest_words))
