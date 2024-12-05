def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted += shift_char
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example Usage
plain_text = "HELLO"
shift_key = 3
cipher_text = encrypt(plain_text, shift_key)
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {decrypt(cipher_text, shift_key)}")
