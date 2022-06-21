import random

comp_c =  random.randint(1,3)
user_c = int(input("Guess Rock(1), Paper(2), or Scissors(3): "))

if comp_c == user_c:
    print("Same Choice, Tie")
elif (comp_c == 1 and user_c == 3) or (comp_c == 2 and user_c == 1) or (comp_c == 3 and user_c == 2):
    print("Computer wins!")
else:
    print("You win!")