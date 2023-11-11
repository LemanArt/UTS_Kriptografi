def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Informasi login
username = "Leman"
password = "asikasik"
key = "apapun"  # Ganti kunci dengan kunci rahasia yang Anda inginkan

# Enkripsi password
encrypted_password = vigenere_encrypt(password, key)
print("")
print("Kata Sandi Terenkripsi (",encrypted_password,")")
print("")

# Simpan username dan password terenkripsi ke dalam file teks
with open("login_info.txt", "w") as file:
    file.write(f"Username: {username}\n")
    file.write(f"Password: {encrypted_password}\n")

print("Informasi login telah disimpan.")

# Kemudian, saat pengguna mencoba masuk
input_username = input("Username: ")
input_password = input("Password: ")

if input_username == username:
    decrypted_password = vigenere_decrypt(encrypted_password, key)
    if input_password == decrypted_password:
        print("Selamat datang, Leman! Anda berhasil masuk.")
    else:
        print("Kata sandi salah. Akses ditolak.")
else:
    print("Username salah. Akses ditolak.")
