import random
import time
import os

numbers = list(range(37))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def spin():
    spins = random.randint(30, 60)
    delay = 0.05

    for i in range(spins):
        clear()
        current = numbers[i % len(numbers)]
        print("Roulette Wheel\n")
        print(f"Spinning... [{current}]")
        time.sleep(delay)
        delay *= 1.05  # slow down

    result = numbers[spins % len(numbers)]
    print(f"\nFinal result: {result}")

spin()