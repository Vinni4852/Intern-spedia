import random
import math
lower_limit=int(input("Enter Lower limit for a range of numbers: "))
upper_limit=int(input("Enter upper limit for a range of numbers: "))
n = random.randint(lower_limit, upper_limit)
print("\nYou've only ",round(math.log(upper_limit - lower_limit + 1, 2)), " chances to guess the integer!\n")
count = 0
while count < math.log(upper_limit - lower_limit + 1, 2):
    count += 1
    guess = int(input("Guess a number: "))

    if n > guess:
        print("You guessed too small!")
    elif n < guess:
        print("You guessed too high!")
    else:
        print("Congratulations! you did it in ", count, " try.")
        break

if count >= math.log(upper_limit - lower_limit + 1, 2):
    print("\nThe number is %d" % n)
    print("\nBetter Luck Next time!")

