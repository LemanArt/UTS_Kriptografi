def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    return next(i for i in range(1, m) if (a * i) % m == 1)

def affine_encrypt_decrypt(text, a, b, decrypt=False):
    m = 26
    transform = lambda x: (a * x + b) % m if not decrypt else (mod_inverse(a, m) * (x - b)) % m

    result = ""
    for char in text:
        if char.isalpha():
            case_offset = ord('a') if char.islower() else ord('A')
            result += chr(transform(ord(char) - case_offset) + case_offset)
        else:
            result += char

    return result

def main():
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    a = int(input("Masukkan nilai a (bilangan bulat relatif prima dengan 26): "))
    b = int(input("Masukkan nilai b (bilangan bulat): "))

    if gcd(a, 26) != 1:
        print("Error: a harus relatif prima dengan 26.")
        return

    encrypted_text = affine_encrypt_decrypt(plain_text, a, b)
    print("Teks terenkripsi:", encrypted_text)

    decrypted_text = affine_encrypt_decrypt(encrypted_text, a, b, decrypt=True)
    print("Teks terdekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
