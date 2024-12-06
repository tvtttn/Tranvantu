print('Trần Văn Tú MSV 235752021610056')
def count_letters_and_digits(sentence):
    letter_count = 0  # Đếm số lượng chữ cái
    digit_count = 0   # Đếm số lượng chữ số
    
    # Duyệt qua từng ký tự trong câu
    for char in sentence:
        if char.isalpha():  # Kiểm tra nếu là chữ cái
            letter_count += 1
        elif char.isdigit():  # Kiểm tra nếu là chữ số
            digit_count += 1
    
    # In kết quả
    print(f"Số chữ cái là: {letter_count}")
    print(f"Số chữ số là: {digit_count}")

# Nhập câu từ người dùng
input_sentence = input("Nhập một câu: ")
count_letters_and_digits(input_sentence)
