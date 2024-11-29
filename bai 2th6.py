print('Trần Văn Tú MSV 235752021610056')
class Hinhchunhat(object):
    # Phương thức khởi tạo (constructor) để khởi tạo chiều dài và chiều rộng
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    # Phương thức tính diện tích
    def area(self):
        return self.dai * self.rong


# Tạo đối tượng Hinhchunhat với chiều dài là 5 và chiều rộng là 3
hcn = Hinhchunhat(5, 3)

# In diện tích của hình chữ nhật
print(hcn.area())
