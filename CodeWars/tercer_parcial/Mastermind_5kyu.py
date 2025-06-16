""""
Introduction
Mastermind or Master Mind is a code-breaking game for two players. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. It resembles an earlier pencil and paper game called Bulls and Cows that may date back a century or more. (Source Wikipedia)

mastermind board

Rules
The Mastermind (computer) will select 4 colours. The colours are randomly selected from ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]. Colours can be duplicated but there will always be exactly 4.

The Mastermind will return an array back to you. For every correctly positioned colour in the array an element of "Black" is returned. For every correct colour but in the wrong position an element of "White" will be returned.

Passing the correct array will pass the Kata test and return "WON!".

Passing an invalid colour will fail the test with the error "Error: you have given an invalid colour!".

Passing an invalid array length will fail the test with the error "Error: you must pass 4 colours!".

Guessing more than 60 times will fail the test with the error "Error: you have had more than 60 tries!".

All colours are capitalised.

The return array will be shuffled!

Task
Your task is to create a method called mastermind() that will take an object called game. The object has already been preloaded so you do not need to worry about it.

Within your method you must pass an array into the game object method .check(). This will evoke the object to check your array to see if it is correct.

Example
If the Mastermind selected the following colours

secret code - red, blue, green, yellow

Then the array you are trying to solve is ["Red", "Blue", "Green", "Yellow"]

So you guess with

guess - red, orange, yellow, orange

["Red", "Orange", "Yellow", "Orange"]

Your method would look like this.

def mastermind(game):
  answer = game.check(["Red", "Orange", "Yellow", "Orange"])
The element 0 => Red is at the correct index so Black is added to the return array. Element 2 => Yellow is in the array but at the wrong index position so White is added to the return array.

The Mastermind would then return ["Black", "White"] (But not necessarily in that order as the return array is shuffled by the Mastermind).

Keep guessing until you pass the correct solution which will pass the Kata.

Check result
To check the Masterminds return value

  answer = game.check(["Red", "Orange", "Yellow", "Orange"])
  print (answer)
Good luck and enjoy!
"""
import itertools
import random


def mastermind(game):
    COLORS = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    MAX_TRIES = 60

    # Generar todas las combinaciones posibles (colores pueden repetirse)
    candidates = list(itertools.product(COLORS, repeat=4))

    tries = 0

    while candidates:
        guess = list(candidates[0])  # toma el primer candidato
        tries += 1

        response = game.check(guess)

        if response.count("Black") == 4:
            return "WON!"

        # Filtrar los candidatos que darían el mismo resultado si fueran el secreto
        def simulate(secret, guess):
            blacks = sum(a == b for a, b in zip(secret, guess))
            whites = sum(min(secret.count(color), guess.count(color)) for color in set(COLORS)) - blacks
            return ["Black"] * blacks + ["White"] * whites

        candidates = [c for c in candidates if sorted(simulate(c, guess)) == sorted(response)]

        if tries >= MAX_TRIES:
            raise Exception("Error: you have had more than 60 tries!")

if __name__ == '__main__':
    print()