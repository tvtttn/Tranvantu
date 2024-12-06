print('Trần Văn Tú MSV 235752021610056')
def sieve_of_eratosthenes(limit):
    # Tạo một mảng đánh dấu các số nguyên tố
    sieve = [True] * (limit + 1)  # True có nghĩa là số đó là nguyên tố
    sieve[0] = sieve[1] = False   # 0 và 1 không phải là số nguyên tố
    
    # Tiến hành sàng số nguyên tố
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:  # Nếu i là số nguyên tố
            for j in range(i * i, limit + 1, i):
                sieve[j] = False  # Đánh dấu các bội số của i là không nguyên tố

    # Lấy các số nguyên tố từ mảng sieve
    primes = [i for i in range(2, limit + 1) if sieve[i]]
    
    return tuple(primes)  # Trả về một tuple các số nguyên tố

# Xác định giới hạn (1 triệu)
limit = 1000000

# Tạo tuple các số nguyên tố nhỏ hơn 1 triệu
prime_tuple = sieve_of_eratosthenes(limit)

# In ra kết quả
print(f"Các số nguyên tố nhỏ hơn 1 triệu là: {prime_tuple}")
