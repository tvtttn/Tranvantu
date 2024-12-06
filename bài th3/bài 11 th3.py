print('Tran Van Tu MSV 235752021610056')
def benefit(t,n,k):
    #chuyển đổi lãi suất từ phần trăm sang số thập phân
    lãi_suất = t / 100
    #tính số tiền sau k tháng
    số_tiền_nhận_được = n * ((1 + lãi_suất) ** k)
    return số_tiền_nhận_được
#nhập dữ liệu từ bàn phím
try:
    t = float(input("nhập lãi suất tiết kiệm (t%/tháng): "))
    n = float(input("nhập số vốn ban đầu (n): "))
    k = float(input("nhập số tháng gửi (k): "))
    #tính số tiền nhận được
    tiền_nhận = benefit(t,n,k)
    print(f"số tiền nhận được sau {k} tháng là: {tiền_nhận:.2f} VNĐ")
except ValueError:
    print("vui lòng nhập giá trị hợp lệ.")
