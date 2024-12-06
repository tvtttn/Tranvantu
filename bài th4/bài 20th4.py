print('Trần Văn Tú MSV 235752021610056')
def pascal_triangle(n):
    # Duyệt qua các dòng từ 0 đến n-1
    for i in range(n):
        # Dòng thứ i của tam giác Pascal
        row = [1] * (i + 1)  # Khởi tạo dòng với tất cả các giá trị bằng 1
        
        # Tính các giá trị trong dòng, bắt đầu từ vị trí thứ 1 và kết thúc ở vị trí thứ (i-1)
        for j in range(1, i):
            row[j] = row[j - 1] + row[j]
        
        # In ra dòng hiện tại
        print(" ".join(map(str, row)))

# Nhập n từ người dùng
n = int(input("Nhập số dòng n của Tam giác Pascal: "))
pascal_triangle(n)
