print('Trần Văn Tú MSV 235752021610056')
class Circle(object):
    # Phương thức khởi tạo (constructor) để khởi tạo bán kính
    def __init__(self, r):
        self.radius = r

    # Phương thức tính diện tích
    def area(self):
        return self.radius ** 2 * 3.14


# Tạo đối tượng Circle với bán kính là 2
aCircle = Circle(2)

# In diện tích của hình tròn
print(aCircle.area())

