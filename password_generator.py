import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generates a random password based on user-specified criteria."""
    
    # Create a pool of characters to choose from
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters  # a-z and A-Z
    if use_numbers:
        char_pool += string.digits        # 0-9
    if use_symbols:
        char_pool += string.punctuation   # !, @, #, $, etc.

    # Check if the character pool is empty
    if not char_pool:
        return "Error: Please select at least one character type."

    # Generate the password by picking random characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    """Main function to get user input and display the password."""
    print("--- Welcome to the Random Password Generator ---")

    try:
        # Get password length from the user
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return

        # Get character type preferences
        use_letters = input("Include letters (y/n)? ").lower() == 'y'
        use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
        use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\n----------------------------------------")
        print(f"Your Generated Password is: {password}")
        print("----------------------------------------")

    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")

# Run the main program
if __name__ == "__main__":
    main()
