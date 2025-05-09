"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""
def remove_exclamation_marks(s):
    word = ""
    for i in s:
        if i != "!":
            word += i
    return word

if __name__ == '__main__':
    print(remove_exclamation_marks("Hello World!"))
    print(remove_exclamation_marks("Hi! Hello!"))