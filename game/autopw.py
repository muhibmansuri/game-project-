import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a random password based on the specified criteria.
    """
    # Ensure minimum length if multiple types are selected
    if length < 4:
        print("Password length updated to 4 for security.")
        length = 4

    character_pool = ""
    required_chars = []

    # Add selected character types to pool and ensure at least one of each is used
    if use_upper:
        character_pool += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    
    if use_lower:
        character_pool += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))

    if use_digits:
        character_pool += string.digits
        required_chars.append(random.choice(string.digits))

    if use_special:
        # You can customize this string to restrict allowed special characters
        special_chars = "!@#$%^&*()-_=+"
        character_pool += special_chars
        required_chars.append(random.choice(special_chars))
    
    if not character_pool:
        return "Error: No character types selected!"

    # Fill the rest of the password length
    remaining_length = length - len(required_chars)
    for _ in range(remaining_length):
        required_chars.append(random.choice(character_pool))

    # Shuffle the result to mix the guaranteed characters with the random ones
    random.shuffle(required_chars)
    
    return "".join(required_chars)

if __name__ == "__main__":
    print("--- Auto Password Generator ---")
    while True:
        try:
            user_input = input("\nEnter password length (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
                
            length = int(user_input)
            if length <= 0:
                print("Please enter a positive number.")
                continue

            password = generate_password(length=length)
            print(f"Generated Password: {password}")
            
        except ValueError:
            print("Invalid input! Please enter a number.")
