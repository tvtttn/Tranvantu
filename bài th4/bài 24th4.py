print('Trần Văn Tú MSV 235752021610056')
def count_upper_and_lower(sentence):
    upper_count = 0  # Đếm số chữ hoa
    lower_count = 0  # Đếm số chữ thường
    
    # Duyệt qua từng ký tự trong câu
    for char in sentence:
        if char.isupper():  # Kiểm tra nếu là chữ hoa
            upper_count += 1
        elif char.islower():  # Kiểm tra nếu là chữ thường
            lower_count += 1
    
    # In kết quả
    print(f"Chữ hoa: {upper_count}")
    print(f"Chữ thường: {lower_count}")

# Nhập câu từ người dùng
input_sentence = input("Nhập một câu: ")
count_upper_and_lower(input_sentence)
