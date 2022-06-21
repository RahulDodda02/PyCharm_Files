import random

num = random.randint(1, 100)
guess = 0
count = 0

while guess != num:
    guess = int(input("Guess a number: "))
    count += 1
    if guess == num:
        break
    elif guess < num:
        print("Too Low!")
    else:
        print("Too High!")

print(f"Congrats, You guessed the number in {count} tries!")