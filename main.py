import random


def askUser():
    minNum = int(input("insert minimum: "))
    maxNum = int(input("insert maximum: "))
    numActual = random.randint(minNum, maxNum)
    difficulty = int(input("choose a diffucly (easy: 1, medium: 2, hard: 3): "))
    if difficulty == 1:
        lives = 9
    elif difficulty == 2:
        lives = 7
    elif difficulty == 3:
        lives = 5


    guessLogic(minNum, maxNum, numActual, lives)


def guessLogic(minNum, maxNum, numActual, lives):
    print("---------------------------------------------------------------------")
    if lives == 0:
        play = input("You are out of lives...would you like to play again? Y/N: ")
        if play == 'Y':
            askUser()
        elif play == 'N':
            quit()

    print(f"you have {lives} lives!")
    guess = int(input(f"Guess the Number between the range {minNum} - {maxNum}: "))
    guess = guess

    if numActual == guess:
        print("Congratulations, you guessed the right number!!!")
        play = input("would you like to play again? Y/N: ")
        if play == 'Y':
            askUser()
        elif play == 'N':
            quit()
    elif guess > maxNum or guess < minNum:
        lives -= 1
        print("The number you guessed was outside the range...try again.")
        guessLogic(minNum, maxNum, numActual, lives)
    elif guess < numActual:
        lives -= 1
        print("WRONG! the number you guessed was low ...try again.")
        guessLogic(minNum, maxNum, numActual, lives)
    elif guess > numActual:
        lives -= 1
        print("WRONG! the number you guessed was high...try again.")
        guessLogic(minNum, maxNum, numActual, lives)
if __name__ == '__main__':
    askUser()
