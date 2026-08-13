def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result


print("===== Caesar Cipher Tool =====")

mode = input("Choose (encrypt/decrypt): ").lower()

message = input("Enter your message: ")

shift = int(input("Enter shift value: "))

output = caesar_cipher(message, shift, mode)

print("Result:", output)