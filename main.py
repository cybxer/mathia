import math

def password_entropy(R, L, in_common_passwords, in_easy_sequences):
    E = math.log2(R**L)
    if in_common_passwords or in_easy_sequences:
        E /= 2  # Reduce entropy if the password is in the common passwords list or easy sequences
    return E

def check_in_common_passwords(password):
    with open('10-million-password-list-top-1000000.txt', 'r') as file:
        if password in file.read():
            return True
    return False

def check_in_easy_sequences(password):
    with open('easy sequences.txt', 'r') as file:
        if password in file.read():
            return True
    return False

R = 62 # Range of characters

password = input("Enter the password: ")
L = len(password)  # Number of characters in password
in_common_passwords = check_in_common_passwords(password)
in_easy_sequences = check_in_easy_sequences(password)
E = password_entropy(R, L, in_common_passwords, in_easy_sequences)
print(f"The password entropy for '{password}' is approximately {E:.2f} bits.")

