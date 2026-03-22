def encrypt(message, shift):
    result = ""

    for letter in message:
        if letter.isupper():
            position = ord(letter) - ord('A')
            shifted = (position + shift) % 26
            result += chr(shifted + ord('A'))

        elif letter.islower():
            position = ord(letter) - ord('a')
            shifted = (position + shift) % 26
            result += chr(shifted + ord('a'))

        else:
            result += letter

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)


print("🔐 Welcome to Caesar Cipher!")
print("=" * 30)

while True:
    choice = input("\nType 'e' to encrypt, 'd' to decrypt or 'q' to quit: ").lower()

    if choice == 'q':
        print("Goodbye!")
        break
        ''
    elif choice in ['e', 'd']:
        message = input ("Enter your message: ");
        shift = int(input("Enter shift number: "))

        if choice =='e':
            result = encrypt(message, shift)
            print("Encrypted message: ", result)
        
        else:
            result = decrypt(message, shift)
            print("Decrypted message: ", result)

else:
    print("Invalid choice. Please type 'e' or 'd' or 'q'.")