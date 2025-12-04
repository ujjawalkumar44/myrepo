import random
import string

def random_number():
    return random.randint(1, 1000)

def random_float():
    return round(random.uniform(1, 100), 2)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def random_name():
    names = ["Arjun", "Riya", "Karanu", "Aisha", "Kabir", "Meera", "Ujjawal", "Saanvi"]
    return random.choice(names)

def main():
    print("Random Number:", random_number())
    print("Random Float:", random_float())
    print("Random Color:", random_color())
    print("Random Password:", random_password())
    print("Random Name:", random_name())

main()

