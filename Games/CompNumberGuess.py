import random

print("Think of a Random Number in between 1 and 100")

maxNum = 100
minNum = 1
correct = False
check = ""

while not correct:
    guess = random.randint(minNum, maxNum)
    check = input(f"is your number {guess}? If yes type Y, if your num is higher type H, if your num is lower type L: ")
    if check == "Y" or check == "y":
        correct = True
    elif check == "H" or check == "h":
        minNum = guess + 1
    elif check == "L" or check == "l":
        maxNum = guess - 1
    else:
        print("Not a valid input!")

print(f"The number is {guess}!")