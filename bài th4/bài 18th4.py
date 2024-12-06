print('Trần Văn Tú MSV 235752021610056')
def fibonacci_list(n):
    fib = []  # Danh sách chứa các số Fibonacci
    a, b = 0, 1  # Hai số đầu tiên trong dãy Fibonacci
    
    while a < n:
        fib.append(a)  # Thêm số a vào danh sách
        a, b = b, a + b  # Cập nhật giá trị a và b
    
    return fib

# Nhập giá trị n từ người dùng
n = int(input("Nhập số n: "))
fib_list = fibonacci_list(n)

# In ra dãy Fibonacci nhỏ hơn n
print("Danh sách các số Fibonacci nhỏ hơn n:", fib_list)
