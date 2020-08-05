#   Guess the number Game

key = 43
count = 10
print("Total guesses left = ", count)
while True:
    guess = input("Enter a number to guess\n")
    if not guess.isnumeric():
        print("Enter a valid number")
        continue
    if int(guess) < key and count > 0:
        print("you need to enter a higher value\n")
        count = count - 1
        print("Total guesses left = ", count)
    elif int(guess) > key:
        print("you need to enter a lower value\n")
        count = count - 1
        print("Total guesses left = ", count)
    elif int(guess) == key:
        print("Congratulations you guessed it right\n")
        break
    elif count == 0:
        print("Game Over\n")
        break
