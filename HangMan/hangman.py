import random

hangmanpics = ['''
        +---+
        |   |
            |
            |
            |
            |
      =========''','''
        +---+
        |   |
        O   |
            |
            |
            |
      =========''','''
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========''','''
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========''','''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========''','''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========''','''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========''']

def strike(text):
    result = text + '\u0336'
    return result

def getRandWord(wordList):
    randWord = wordList[random.randrange(len(wordList))]
    return list(randWord)

def genDashLines(word):
    dash = ' - ' * len(word)
    return dash.split()

def getGuess(alreadyGuessed):
    while True:
        print('\n', 'Guess a letter: ', end='')
        guess = input().lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You already guessed that letter. Try again.")
        elif not (guess.isalpha()):
            print("Please enter a LETTER.")
        else:
            return guess

def displayBoard(hangmanpics, missedLetters, correctLetters, secretWord, alphabet, dashLines):
    alreadyGuessed = missedLetters + correctLetters

    print(hangmanpics[len(missedLetters)])

    for i in range(len(alphabet)):
        if alphabet[i] in alreadyGuessed:
            alphabet[i] = strike(char[i])

    for i in range(len(alphabet)):
        if i < 12:
            print(alphabet[i], end=' ')
        elif i == 12:
            print(alphabet[i], "\n")
        elif i > 12:
            print(alphabet[i], end=' ')

    for i in range(len(alphabet)):
        if char[i] in alreadyGuessed:
            char[i] = strike(char[i])

    # print(alphabet, "\n")

    print("\n\n", dashLines)

def playAgain():
    print('\n', 'Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def startGame():
    secretWord = getRandWord(words)
    dashLines = genDashLines(secretWord)
    missedLetters = ""
    correctLetters = ""
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    char = alphabet.split()
    gameIsDone = False
    return (secretWord, dashLines, missedLetters, correctLetters, char, gameIsDone)

# Get all words into a list
wordsList = open('words.txt', 'r')
words = wordsList.read().lower().split()

print("H A N G M A N")
secretWord, dashLines, missedLetters, correctLetters, char, gameIsDone = startGame()
print(secretWord)

while True:
    displayBoard(hangmanpics, missedLetters, correctLetters, secretWord, char, dashLines)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        for i in range(len(secretWord)):
            if guess == secretWord[i]:
                dashLines[i] = guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\n', 'You Won! The word is indeed: ', end = '')
            print('[', ''.join(secretWord), ']')
            gameIsDone = True
    else:
        missedLetters += guess

        if len(missedLetters) == len(hangmanpics) - 1:
            displayBoard(hangmanpics, missedLetters, correctLetters, secretWord, char, dashLines)

            print('\n', 'You FAILED! The word was: ', end = '')
            print('[', ''.join(secretWord), ']')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            secretWord, dashLines, missedLetters, correctLetters, char, gameIsDone = startGame()
        else:
            break
