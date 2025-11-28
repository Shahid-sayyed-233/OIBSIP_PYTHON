import random
import string

def get_valid_length():
    while True:
        try:
            length = int(input("Enter password length (4-64): "))
            if 4 <= length <= 64:
                return length
            else:
                print("⚠️ Length must be between 4 and 64.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def get_character_sets():
    chars = ""
    include_letters = input("Include letters? (y/n): ").lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    if include_letters:
        chars += string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if not chars:
        print("⚠️ You must select at least one character set.")
        return get_character_sets()
    return chars

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("=== Random Password Generator ===")
    length = get_valid_length()
    chars = get_character_sets()
    password = generate_password(length, chars)
    print(f"\n🔑 Your generated password: {password}")

if __name__ == "__main__":
    main()