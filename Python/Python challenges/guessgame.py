import random
print("Guess the number between 1 to 50")
n = random.randint(1, 51)
guess = 9
while True:
    if guess == 0:
        print("Game over")
        break
    else:
        print("you have", guess, "guesses left")
    num = int(input("Enter your guess :"))
    guess = guess - 1
    if num > n:
        print("Hint: Number is lower")
    elif num < n:
        print("Hint: Number is greater")
    else:
        print("You won with", guess, "guesses left")
        break
