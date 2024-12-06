print('Trần Văn Tú MSV 235752021610056')
class RomanToInt:
    def __init__(self, roman):
        self.roman = roman
        # Bảng các ký tự La Mã và giá trị tương ứng
        self.roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def to_int(self):
        total = 0
        length = len(self.roman)

        for i in range(length):
            # Lấy giá trị của ký tự hiện tại
            current_value = self.roman_dict[self.roman[i]]

            # Nếu ký tự hiện tại nhỏ hơn ký tự sau đó, chúng ta trừ đi
            if i + 1 < length and current_value < self.roman_dict[self.roman[i + 1]]:
                total -= current_value
            else:
                total += current_value

        return total


# Sử dụng class để chuyển đổi số La Mã
roman = "IX"  # Ví dụ: Số La Mã "IX" tương ứng với số nguyên 9
converter = RomanToInt(roman)
result = converter.to_int()
print(f"Số nguyên tương ứng với {roman} là {result}")
