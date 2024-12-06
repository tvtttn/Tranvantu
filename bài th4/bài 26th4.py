print('Trần Văn Tú MSV 235752021610056')
def calculate_balance():
    balance = 0  # Khởi tạo số dư ban đầu là 0
    
    # Nhập vào giao dịch từ người dùng
    print("Nhập nhật ký giao dịch (D <số tiền> để gửi, W <số tiền> để rút). Nhập 'x' để kết thúc.")
    
    while True:
        transaction = input("Nhập giao dịch: ").strip()
        
        if transaction.lower() == 'x':  # Nếu nhập 'x' thì dừng chương trình
            break
        
        # Phân tách loại giao dịch và số tiền
        parts = transaction.split()
        if len(parts) != 2:
            print("Giao dịch không hợp lệ. Vui lòng nhập lại.")
            continue
        
        action, amount_str = parts
        try:
            amount = int(amount_str)  # Chuyển số tiền thành số nguyên
        except ValueError:
            print("Số tiền không hợp lệ. Vui lòng nhập lại.")
            continue
        
        if action == 'D':  # Gửi tiền
            balance += amount
        elif action == 'W':  # Rút tiền
            balance -= amount
        else:
            print("Loại giao dịch không hợp lệ. Vui lòng nhập lại.")
    
    print("Số tiền thực trong tài khoản là:", balance)

# Gọi hàm tính toán số dư tài khoản
calculate_balance()
