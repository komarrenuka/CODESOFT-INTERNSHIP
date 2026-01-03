import random
import string

def generate_password(length):
    # Define the possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask the user for password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Generate and display the password
password = generate_password(length)
print("Generated password:", password)
