print('Tran Van Tu MSV 235752021610056')
import math
def Tinh(R):
    #kiểm tra giá trị bán kính hợp lệ
    if R <= 0:
        return "bán kính phải lớn hơn 0."
    #tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * (R ** 2)
    return f"chu vi hình tròn: {chu_vi:.2ef}\n Diện tích hình tròn: {dien_tich:.2f}"
#Nhập từ bán kính từ bàn phím
try:
    R = float(input("nhập bán kính hình tròn: "))
    result = Tinh(R)
    print(result)
except ValueError:
    print("vui lòng nhập một số hợp lệ.")
    
