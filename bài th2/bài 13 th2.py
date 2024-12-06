input("Tran Van Tu MSV 235752021610056")
#giải phương trình bậc hai 2:ax^2+bx+c=0
from math import sqrt
a = float(input("Nhap tham so a = "))
b = float(input("Nhap tham so b = "))
c = float(input("Nhap tham so c = "))
d = b*b - 4*a*c
#neu d<0 thi PTVN
#nguoc lai neu d=0 thi pt co 1 nghiem
#nguoc lai pt co 2 nghiem
if d<0:
    print("phuong trinh vo nghiem")
elif d==0:
    print("phuong trinh co 1 nghiem: ",-b/(2*a))
else:
    print("phuong trinh co 2 nghiem: ")
    x1= (-b - sqrt(d))/(2*a)
    x2= (-b + sqrt(d))/(2*a)
    print("x1=",x1)
    print("x2=",x2)
