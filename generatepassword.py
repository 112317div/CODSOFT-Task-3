import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from 1, 2, or 3.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password: ", password)
    return password

# Take user input for the length and complexity of the password
password_length = int(input("Enter the length of the password: "))
password_complexity = int(input("Enter the complexity level (1 for letters, 2 for letters and digits, 3 for letters, digits, and punctuation): "))
generated_password = generate_password(password_length, password_complexity)
