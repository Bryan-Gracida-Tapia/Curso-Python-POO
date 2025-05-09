"""
Take an array and remove every second element from the array. Always keep the first
element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""

def remove_every_other(my_list):
    return my_list[::2] # : (empieza desde el inicio) : (hasta el final) 2 (saltando de dos en dos)

if __name__ == '__main__':
    print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
    print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
