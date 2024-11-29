print('Trần Văn Tú MSV 235752021610056')
class ATM:
    def __init__(self, pin, balance):
        self.pin = pin  # Mã PIN của tài khoản
        self.balance = balance  # Số dư tài khoản

    # Phương thức kiểm tra mã PIN
    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    # Phương thức kiểm tra và rút tiền
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rút tiền thành công: {amount} VNĐ.")
            print(f"Số dư hiện tại: {self.balance} VNĐ.")
        else:
            print("Số dư không đủ để rút tiền.")

    # Phương thức kiểm tra số dư
    def check_balance(self):
        print(f"Số dư tài khoản của bạn là: {self.balance} VNĐ.")

    # Phương thức chuyển tiền
    def transfer(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Chuyển khoản thành công: {amount} VNĐ.")
            print(f"Số dư còn lại: {self.balance} VNĐ.")
        else:
            print("Số dư không đủ để chuyển khoản.")

# Hàm để thực hiện giao dịch ATM
def atm_transaction():
    # Tạo tài khoản ATM với mã PIN là '1234' và số dư ban đầu là 100000 VNĐ
    atm = ATM(pin="1234", balance=100000)

    # Đăng nhập
    entered_pin = input("Nhập mã PIN: ")
    if not atm.check_pin(entered_pin):
        print("Mã PIN không chính xác. Vui lòng thử lại.")
        return

    # Sau khi đăng nhập thành công, cho phép người dùng chọn giao dịch
    while True:
        print("\nChọn giao dịch:")
        print("1. Rút tiền")
        print("2. Chuyển khoản")
        print("3. Kiểm tra số dư")
        print("4. Thoát")

        choice = input("Nhập lựa chọn (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Nhập số tiền muốn rút: "))
            atm.withdraw(amount)
        elif choice == "2":
            amount = float(input("Nhập số tiền muốn chuyển khoản: "))
            atm.transfer(amount)
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ ATM. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Chạy chương trình ATM
atm_transaction()
