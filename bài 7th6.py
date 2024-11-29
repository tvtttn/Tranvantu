print('Trần Văn Tú MSV 235752021610056')
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo bán kính hình tròn

    # Phương thức tính diện tích
    def area(self):
        return math.pi * (self.radius ** 2)

    # Phương thức tính chu vi
    def perimeter(self):
        return 2 * math.pi * self.radius


# Tạo đối tượng Circle với bán kính 5
circle = Circle(5)

# Tính diện tích và chu vi của hình tròn
print(f"Diện tích hình tròn: {circle.area():.2f}")
print(f"Chu vi hình tròn: {circle.perimeter():.2f}")
