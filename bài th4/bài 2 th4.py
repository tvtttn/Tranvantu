print('Tran Van Tu MSV 23572021610056')
def print_visible_chars(input_string):
    for char in input_string:
        if char not in [' ', '\t']: #bỏ qua dấu space và dấu tab
            print(char , end=' ')
#ví dụ sử dụng
input_string = "Hello\tworld! This is a test string.\n"
print_visible_chars(input_string)
