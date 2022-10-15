import string
import random

characters = list(string.ascii_letters + string.digits + "0123456789")


def generate_random_password(length: int):
    #length = int(input("Enter password length: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


if __name__ == '__main__':
    a = input("Length: ")
    if a == "":
        a = 8
    for i in range(20):
        print(generate_random_password(a))

