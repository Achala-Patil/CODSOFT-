import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type should be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def prompt_user_for_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Error: Length should be a positive integer.")
            else:
                return length
        except ValueError:
            print("Error: Please enter a valid integer.")

def prompt_user_for_options():
    print("Choose which character types to include in the password:")
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    return use_lowercase, use_uppercase, use_digits, use_special_chars

def main():
    print("Welcome to Password Generator")

    while True:
        length = prompt_user_for_length()
        use_lowercase, use_uppercase, use_digits, use_special_chars = prompt_user_for_options()

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        if password:
            print("Generated Password:", password)

        continue_or_exit = input("Do you want to generate another password? (yes/no): ")
        if continue_or_exit.lower() != 'yes':
            print("Thank you for using Password Generator!!")
            break

if __name__ == "__main__":
    main()