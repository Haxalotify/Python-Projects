"""Generates names by randomly combining names from 2 seperate lists"""
import sys, random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")
    first = ('Baby Oil', 'Bad News', 'Big Burps')
    last = ('Appleyard', 'Bigmeat', 'Bloominshine')

    while True:
        firstName = random.choice(first)
        lastName = random.choice(last)

        print("\n\n") #new line for readability
        print("{} {}".format(firstName, lastName), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break #to quit the program otherwise it runs until user inputs "n"
    input("\nPress Enter to exit.")
if __name__ == "__main__":
    main()
