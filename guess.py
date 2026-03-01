import random
number = random.randint(1, 100)
attempt = 0

while (True):
    n = int(input("Guess the number: "))
    attempt += 1
    if (n > number):
        print("Too High")
    elif (n < number):
        print("Too Low")
    elif (n == number):
        print("Congratulations !!!!")
        print("You guessed the correct number in attempt: ", attempt)
        break
