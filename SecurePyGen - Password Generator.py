import secrets
import string
import threading

# Key Features:
# 1. Generates a secure password with customizable length and option to include symbols.
# 2. Automatically copies the generated password to the clipboard for easy use.
# 3. Clears the clipboard after a specified delay for added security.
# 4. Uses ANSI escape codes for colored terminal output for better readability.
# 5. Handles missing dependencies gracefully and provides installation instructions.

# Installation Notes:
# Before running this script, ensure you have the 'pyperclip' module installed for clipboard operations.
# Install 'pyperclip' using pip with the command:
# pip install pyperclip
# Depending on your system, you might need to use pip3 instead of pip.
# This script uses ANSI escape codes to display colored text in the terminal. These codes work in most Unix and Unix-like terminals.

try:
    import pyperclip
except ImportError:
    print("\033[91m" + "This script requires the 'pyperclip' module." + "\033[0m")  # Red text
    print("Please install it by running 'pip install pyperclip', then rerun the script.")
    exit()

def generate_secure_password(length=12, include_symbols=True):
    """
    Generates a secure password.

    Parameters:
    length (int): The desired length of the password.
    include_symbols (bool): Whether to include symbols in the password.

    Returns:
    str: A securely generated password.
    """
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def clear_clipboard_after_delay(delay):
    """
    Clears the clipboard content after a specified delay and notifies the user.

    Parameters:
    delay (int): The delay in seconds before the clipboard is cleared.
    """
    def clear_clipboard():
        pyperclip.copy("")  # Clear clipboard
        print("\033[92m" + "\nClipboard has been cleared for your security. Exiting the program is now safe." + "\033[0m")  # Green text
        # Security Note: Depending on your system and environment, the clipboard might not be accessible or could be monitored by other applications. Always ensure sensitive information is handled securely.

    threading.Timer(delay, clear_clipboard).start()
    print("\033[91m" + f"NOTE: DO NOT press Enter or close the program. The program will quit automatically, and the Clipboard will be cleared in {delay} seconds for your security." + "\033[0m")  # Red text

def main():
    print("Secure Password Generator Script")
    print("Follow the prompts to generate a secure password that will be copied to your clipboard.")
    
    try:
        password_length = int(input("Enter the desired length of the password: "))
        include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_secure_password(length=password_length, include_symbols=include_symbols)
        print(f"\033[92mGenerated Password: {password}\033[0m")  # Green text
        pyperclip.copy(password)
        print("Password copied to clipboard.")

        # Schedule the clipboard to be cleared after 60 seconds for security.
        clear_clipboard_after_delay(60)
        
    except ValueError:
        print("\033[91mPlease enter a valid integer for the password length.\033[0m")  # Red text
    except Exception as e:
        print(f"\033[91mAn unexpected error occurred: {e}\033[0m")  # Red text

if __name__ == "__main__":
    main()
    
    # Security Considerations:
    # - The script uses the 'secrets' module for secure random number generation, suitable for managing passwords or cryptographic keys.
    # - Clipboard data is cleared automatically for security, but users should be aware of the potential for clipboard data to be accessed by other applications.
    
