# List of common passwords (dictionary)
password_list = ["123456", "password", "admin", "welcome", "letmein", "qwerty"]

# The actual password to crack (for demo purposes)
target_password = "letmein"

def crack_password(password_list, target_password):
    for password in password_list:
        print(f"Trying password: {password}")
        if password == target_password:
            print(f"Password cracked! The password is: {password}")
            return
    print("Password not found in the list.")

# Run the dictionary attack
crack_password(password_list, target_password)
