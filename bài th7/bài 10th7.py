print('Trần Văn Tú MSV 235752021610056')
import string

def find_longest_words(text):
    # Tách văn bản thành các từ và loại bỏ dấu câu
    words = text.split()
    words = [word.strip(string.punctuation) for word in words]  # Loại bỏ dấu câu

    # Tìm độ dài lớn nhất của các từ
    max_length = max(len(word) for word in words)

    # Lọc ra những từ có độ dài bằng độ dài lớn nhất
    longest_words = [word for word in words if len(word) == max_length]

    return longest_words, max_length

# Đọc văn bản từ người dùng
text = input("Nhập văn bản: ")

# Gọi hàm để tìm những từ dài nhất
longest_words, max_length = find_longest_words(text)

# Hiển thị kết quả
print(f"Các từ dài nhất có độ dài {max_length}: {', '.join(longest_words)}")
