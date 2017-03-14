import random

def getGuess(randNum):
    while True:
        print('\n', 'What is my number? ', end='')
        guess = input()
        if guess.isalpha():
            print("You can only input numbers.")
        elif int(guess) < randNum:
            print("Your guess is SMALLER than my number!")
        elif int(guess) > randNum:
            print("Your guess is BIGGER than my number!")
        else:
            return int(guess)

def playAgain():
    print('\n', 'Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def startGame():
    print('''
      ___
     |__ \\
       / /
      |_|
      (_) What is my number (1-1000)''')

    randNum = random.randrange(0, 1001)
    gameIsDone = False
    return randNum, gameIsDone

randNum, gameIsDone = startGame()

while True:
    guess = getGuess(randNum)


    if guess == randNum:
        print("You Won! The number is indeed: ", guess)
        gameIsDone = True

    if gameIsDone:
        if playAgain():
            randNum, gameIsDone = startGame()
        else:
            break

