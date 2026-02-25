import random
first = random.randint(1 , 9)
second = random.randint(0 , 9)

def generate_number():
    number = (first * 10) + second
    return number