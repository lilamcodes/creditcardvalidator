import random

def reverse():
    x = [random.choice(range(10)) for i in range(16)]

    while sum(x) % 10 != 0:
        x = [random.choice(range(10)) for i in range(16)]

    print(x)

reverse()