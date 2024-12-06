print('Trần Văn Tú MSV 235752021610056')
# Class cơ sở Nguoi
class Nguoi(object):
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    # Phương thức chung cho tất cả các class con, mặc định sẽ không làm gì
    def getGender(self):
        pass


# Class con Nam kế thừa từ Nguoi
class Nam(Nguoi):
    def __init__(self, ten, tuoi):
        # Gọi constructor của class cơ sở Nguoi
        super().__init__(ten, tuoi)

    # Ghi đè phương thức getGender để in "Nam"
    def getGender(self):
        print("Nam")


# Class con Nu kế thừa từ Nguoi
class Nu(Nguoi):
    def __init__(self, ten, tuoi):
        # Gọi constructor của class cơ sở Nguoi
        super().__init__(ten, tuoi)

    # Ghi đè phương thức getGender để in "Nữ"
    def getGender(self):
        print("Nữ")


# Tạo đối tượng Nam và Nu
nam = Nam("John", 25)
nu = Nu("Jane", 22)

# In giới tính của Nam và Nu
nam.getGender()  # In "Nam"
nu.getGender()  # In "Nữ"
