"""
The intended purpose of this programme is to use various methods in generating a strong passsword for a user. 
Although it is not perfect, I combined caesar cipher with a powerful hashing algorithm developed by a few individuals-
from the unersity of Luxembourg. Here is a link for reference: https://en.wikipedia.org/wiki/Argon2. 

Feel free to review my code and give me any ideas or problems you may notice that can improve the robustness. 

"""

import time
from argon2 import PasswordHasher

ph = PasswordHasher()
hashed_password = ph.hash("password")

class HashingClass:
    def __init__(self, PasswordHasher, complex_num, real_part, imag_part):
        self.PasswordHasher = PasswordHasher
        self.complex_num = complex(real_part, imag_part)
        self.hashed_password = self.PasswordHasher.hash("password")

# using exception handling
try:
    real_part = float(input("Enter the real part of a complex number: "))
    imag_part = float(input("Enter the imaginary part of a complex number: "))   #assume 0 as the input for imaginary part
    complex_num = complex(real_part, imag_part)
except ValueError:
    print("Error: Invalid input for complex number.")

# creating an instance of HashingClass
your_instance = HashingClass(ph, complex_num, real_part, imag_part)

# Print the created instance details
print("Complex Number:", your_instance.complex_num)
print("Hashed Password:", your_instance.hashed_password)

class ComplexHasher:
    def __init__(self):
        self.ph = PasswordHasher()

    def hash_with_complex(self, password):
        hashed_result = ""
        for i, char in enumerate(password):
            # Use the index as the real part and 0 as the imaginary part
            real_part = i
            imag_part = 0

            # Combine real and imaginary parts
            complex_num = complex(real_part, imag_part)

            # Convert complex number to a string representation
            complex_str = f"{complex_num.real}_{complex_num.imag}"

            # Combine password character and complex number string
            data_to_hash = f"{char}_{complex_str}"

            # Hash the combined data using Argon2
            hashed_result += self.ph.hash(data_to_hash)

        return hashed_result

# Example usage:
complex_hasher = ComplexHasher()

# Password from user input
password = input("Enter password: ")

# Hash the password with the complex number for each character's index
hashed_result = complex_hasher.hash_with_complex(password)

print("Hashed Result:", hashed_result)

def caesar_julius(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def secret_key():
    password = input("Create password: ")
    password_encrypted = caesar_julius(password, shift=3)
    with open("password.txt", "w") as file:
        file.write(password_encrypted)

def password_alphabet():
    return "".join(chr(char) for char in range(97, 123))

letter_password = password_alphabet() + " @ "  # Concatenating "@" to the end of the password 

max_attempts = 5
i = 0

while i < max_attempts:                               # Defensive programming attempt using try-except 
    try:
        password_user = input("Please enter password: ")

        if password_user == letter_password:
            print("Password valid")
            break
        else:
            print(f"Password invalid. Attempt {i + 1}")
            i += 1
            if i < max_attempts:
                time.sleep(3)  # Sleep for 3 seconds between attempts
    except ValueError:
        print("Error: Check if the password is invalid")

if i == max_attempts:
    print(f"Maximum number of attempts ({max_attempts}) reached. Exiting.")
