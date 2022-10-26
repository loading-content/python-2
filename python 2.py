import random
import time
import re
from re import finditer

print("\nWelcome to Hangman game\n")

galgje = [
    " +---+ \n" "     | \n" "     | \n" "     | \n" "   ==== \n",
    " +---+ \n" " 0   | \n" "     | \n" "     | \n" "   ==== \n",
    " +---+ \n" " 0   | \n" " |   | \n" "     | \n" "   ==== \n",
    " +---+ \n" " 0   | \n" "/|   | \n" "     | \n" "   ==== \n",
    " +---+ \n" " 0   | \n" "/|\\  | \n" "     | \n" "   ==== \n",
    " +---+ \n" " 0   | \n" "/|\\  | \n" "/    | \n" "   ==== \n",
    " +---+ \n" " 0   | \n" "/|\\  | \n" "/ \\  | \n" "   ==== \n",
]


def main() -> None:
    global count
    global display
    global word
    global word1
    global already_guessed
    global length
    global play_game
    words = [
        "ass",
        "ant",
        "baboon",
        "badger",
        "bat",
        "bear",
        "beaver",
        "camel",
        "cat",
        "clam",
        "cobra",
        "cougar",
        "coyote",
        "crow",
        "deer",
        "dog",
        "donkey",
        "duck",
        "eagle",
        "ferret",
        "fox",
        "frog",
        "goat",
        "goose",
        "hawk",
        "lion",
        "lizard",
        "llama",
        "mole",
        "monkey",
        "moose",
        "mouse",
        "mule",
        "newt",
        "otter",
        "owl",
        "panda",
        "parrot",
        "pigeon",
        "python",
        "rabbit",
        "ram",
        "rat",
        "raven",
        "rhino",
        "salmon",
        "seal",
        "shark",
        "sheep",
        "skunk",
        "sloth",
        "snake",
        "spider",
        "stork",
        "swan",
        "tiger",
        "toad",
        "trout",
        "turkey",
        "turtle",
        "weasel",
        "whale",
        "wombat",
        "zebra",
    ]
    word = random.choice(words)
    word1 = word
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""


def hangman() -> str:
    global count
    global display
    global word
    global word1
    global already_guessed

    limit = 6
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    if len(guess) == 0 or len(guess) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:

        # Gebruik regex om te zoeken en posities te bepalen
        for match in finditer(guess, word1):
            # Geeft terug waar de letters staan in de string
            # print(match.span()[0])
            index = word.find(guess)

            # Replace hier op basis van de match die we hebben gevonden
            display = (
                display[: match.span()[0]] + guess + display[match.span()[0] + 1 :]
            )
        # for loop is echt niet efficient en moet je niet gebruiken !

        # for letter in range(length):
        # print(letter)
        # index = word.find(guess)
        # word = word[:index] + "_" + word[index + 1 :]
        # display = display[:index] + guess + display[index + 1 :]

        already_guessed.extend([guess])
        print(display + "\n")
    elif guess in already_guessed:
        print("You already guessed this letter.\n")
    else:
        count += 1
        already_guessed.extend([guess])
        if count == 1:
            time.sleep(1)
            print(galgje[count])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print(galgje[count])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print(galgje[count])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print(galgje[count])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print(galgje[count])
            print("Wrong guess. " + " last guess remaining\n")
        elif count == 6:
            time.sleep(1)
            print(galgje[count])
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word1)
    if word == display:
        print("Congrats! You have guessed the word correctly!")
        print("The word was:", word1)
        exit()
    elif count != limit:
        hangman()


main()
hangman()
