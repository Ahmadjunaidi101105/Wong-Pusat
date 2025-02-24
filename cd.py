import itertools

# Kata sandi yang ingin dicoba (hanya huruf kecil a-z, panjang maksimal 4)
characters = 'abcdefghijklmnopqrstuvwxyz'
password_length = range(1, 5)  # Mencoba panjang 1 sampai 4 karakter

# Kata sandi target (ganti dengan kata sandi yang ingin dites)
target_password = "abc"

# Mencoba semua kombinasi
for length in password_length:
    for attempt in itertools.product(characters, repeat=length):
        attempt = ''.join(attempt)
        print(f"Mencoba: {attempt}")
        if attempt == target_password:
            print(f"Kata sandi ditemukan: {attempt}")
            break
    else:
        continue
    break