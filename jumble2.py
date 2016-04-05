import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
##setting up a list of words

def instructions():
    print "Unscramble the letters to make a word. (Press enter key at the prompt to quit.)"
##prints instructions
    
def random_word():
    word = random.choice(WORDS)
    return word
##chooses a random word from the list

def jumble(word):
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position +1):]
    return jumble
##jumbles the word

def play(word,jumble):
    print "The jumble is: ", jumble
##says what the jumbled version is

#getting the player's guess

    guess = raw_input("\nYour guess: ")
    guess = guess.lower()
    while (guess != word) and (guess != ""):  
        if guess == "hint":   ##provides a hint
            print "The word begins with: " + str(hint) + "."
            guess = raw_input("Your guess: ")
            guess = guess.lower()
            if guess == word:
                print "That's it! You guessed it! \n"
        else:
            print "Sorry, that's not it."
            guess = raw_input("Your guess: ")
            guess = guess.lower()
            if guess == word:
                print "That's it! You guessed it! \n"

    print "Thanks for playing."

##putting the functions together
def main():
    instructions()
    the_word = random_word()
    the_jumble = jumble(the_word)
    play(the_word, the_jumble)

main()
##calling the function to begin the game
