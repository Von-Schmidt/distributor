import random
import string

def generate_password(length):
    all_chars = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    password = [random.choice(chars) for chars in all_chars]
    password += random.choices(''.join(all_chars), k=length-4)
    random.shuffle(password)
    return ''.join(password)

