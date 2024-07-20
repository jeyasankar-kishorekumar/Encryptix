import random
import string

def generate_password(length):
    #It Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #It Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        
        # Ensure the password length is reasonable
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
if __name__ == "__main__":
    main()
