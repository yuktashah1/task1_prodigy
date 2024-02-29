#!/usr/bin/env python
# coding: utf-8

# In[1]:


def caesar_cipher(text, shift):

    result = ""
    for char in text:
        if char.isalpha():  
            if char.islower():  
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else: 
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:  
            result += char
    return result

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, -shift) 
            print("Decrypted message:", decrypted_message)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


# In[ ]:




