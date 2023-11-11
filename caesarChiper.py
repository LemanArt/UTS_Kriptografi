def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shifted_index = (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26
            result += chr(shifted_index + ord('a' if char.islower() else 'A'))
        else:
            result += char

    return result


while True:
    print("Pilih tindakan Anda:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    choice = input("Masukkan pilihan Anda (1/2/3): ")

    if choice == "1":
        text = input("Masukkan teks yang ingin Anda enkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (contoh: 3): "))
        encrypted_text = caesar_cipher(text, shift)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == "2":
        text = input("Masukkan teks yang ingin Anda dekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (contoh: 3): "))
        decrypted_text = caesar_cipher(text, -shift)
        print("Teks terdekripsi:", decrypted_text)
    elif choice == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
