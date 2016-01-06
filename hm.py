import sys
import time
import random


class Game(object):

    def __init__(self, word, revealed):
        self.word = word
        self.revealed = revealed
        self.strikes = 0
        self.hints = 0
        self.already_guessed = []


    def hangman(self):
        
        # As long as there is a blank space in the "revealed" list,
        #  the user continues to guess letters, unless strikes > 5 
        #  or the user guesses the whole word
        while '_' in self.revealed and self.strikes < 5:

            guess = self.make_guess()

            if self.strikes == 5:
                break

            elif guess == None:
                pass
            
            # If the user guesses the whole word correctly, 
            # 'revealed' variable set to 'word', which allows 
            #  the winning outcome condition to be met.
            elif len(guess) > 1:
                print "You guessed '%s'\n" % (''.join(guess))
                if guess == self.word:
                    self.revealed = self.word 
                break

            elif guess in self.already_guessed:
                print "You've already guessed that letter!"

            elif guess in self.word:

                print "Nice! '%s' is in the word" % guess

                for index, letter in enumerate(self.word):            
                    if guess == letter:
                        self.revealed[index] = guess
                        self.already_guessed.append(guess)
               
            elif guess not in self.word and self.strikes < 5:
                print "Sorry '%s' not found!...." % guess

                self.strikes += 1
                self.already_guessed.append(guess)

            else:
                return 
        
        self.outcome()

    def outcome(self):
        # Losing outcome if strikes >= 5        
        if self.strikes >= 5:
            print  "*" * 10, "    STRIKE 5!     ", "*" * 10
            print  "*" * 10, " SORRY, YOU LOSE. ", "*" * 10   
            self.reveal_word()

            # returns to starting menu
            return 

        # Winning outcome if no empty slots left for guessing
        elif '_' not in self.revealed:
            self.reveal_word()
            print "*" * 10, " CONGRATS, Ya Got It! ", "*" * 10

            return 
        
        # Losing outcome if the wrong word was guessed  
        else:
            print "Sorry....You Lose."
            self.reveal_word()
            
            # returns to starting menu
            return

    def make_guess(self):
        """
        Provides Strikes and Hints status.
        Then gets choice from user (a guess or a hint).
        """
        
        # Provides game status to user
        print '_' * 40
        print
        print ">>>>>>> STRIKES: %d/5 <<<<<<<" % self.strikes
        print ">>>>>>>  HINTS:  %d/3 <<<<<<<" % self.hints

        # Prints letters user has already guessed;
        #  set() used to only give a particular letter once,
        #  list() used to put those unique letters in a list,
        #  sorted() provides them in alphabetical order.
        print "Already Guessed Letters: ", ' '.join(sorted(list(set(self.already_guessed)))) 
        print "\nTHE BOARD:"
        print ' '.join(self.revealed) 
        print
        print "Guess a letter or the word"
        print "To get a hint, enter '#hint':"
        
        guess = raw_input("> ").lower()
        
        # Creates blank space to distinguish turns in the game from eachother
        print "\n" * 5 
        print "_" * 40
        print

        # If user asks for a hint, assign result of give_hint() to guess variable
        if '#hint' in guess:
            guess = self.give_hint() 

        return guess
            
    
    def give_hint(self):
        """Fills in one of the missing letters for the user."""
        while self.hints < 3:
                
                # Shuffles and loops through letters in the secret word 
                # until it finds one the user hasn't already guessed
                shuffled_word = random.sample(self.word, len(self.word))
                for letter in shuffled_word:
                    if letter not in self.revealed:
                        self.hints += 1
                        print "\n      HINT: '%s'    " % letter
                        print "   Hints used: %d/3  " % self.hints
                        return letter  
        
        print "SORRY %d/3 hints used" % self.hints 
        return 

    def reveal_word(self):
        """Prints out the secret word letter by letter"""

        print "THE SECRET WORD IS:",
        
        for i in range(6):
            sys.stdout.write('. ',)
            sys.stdout.flush()
            time.sleep(.3)
        
        for letter in self.word:
            sys.stdout.write(letter,)
            sys.stdout.flush()
            time.sleep(.3)
        print
        
        return


def start():
    while True:
        # opens enable1.txt file and assign random word to variable 'word'
        word_list = open("enable1.txt", 'r').readlines()
        word = random.choice(word_list).replace('\n','').replace('\r','')
        
        # sets 'revealed' variable to '_'s the length of the chosen random word
        revealed = ['_' for i in range(len(word))]

        print
        choice = raw_input("Press 'Y' to Play\nOr 'Q' to Quit: ")
        if choice.lower() == "y":
            hangman = Game(word, revealed)
            hangman.hangman()
        else:
            print "Goodbye!"
            sys.exit()


if __name__ == "__main__":
    print
    print "Welcome to HANGMAN."
    print "-------------------"
    start()




