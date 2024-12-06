print('Trần Văn Tú MSV 235752021610056')
def tong_uoc(m):
    tong = 0
    for i in range(1, m + 1):
        if m % i == 0:
            tong += i
    return tong

def in_so_nho_hon_n(n):
    for m in range(1, n):
        if tong_uoc(m) > m:
            print(m)

# Nhập giá trị n từ người dùng
n = int(input("Nhập số n: "))
in_so_nho_hon_n(n)
