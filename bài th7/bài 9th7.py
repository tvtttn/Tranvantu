print('Trần Văn Tú MSV 235752021610056')
import shutil

def copy_file( A, B):
    shutil.copyfile(A, B)

# Gọi hàm sao chép
copy_file('A.txt', 'B.txt')
