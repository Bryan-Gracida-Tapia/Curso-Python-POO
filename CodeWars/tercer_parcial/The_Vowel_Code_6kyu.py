""""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


"""
def encode(text: str) -> str:
    mapping = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    return ''.join(mapping.get(char, char) for char in text) #Se recorre cada char en el texto original (for char in text). Además Se reemplaza con el número correspondiente si es una vocal, o se deja igual si no lo es (mapping.get(char, char)).
    #''.join(...) toma esa secuencia y la convierte en un solo string sin espacios.
def decode(text: str) -> str:
    reverse_mapping = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    return ''.join(reverse_mapping.get(char, char) for char in text)


if __name__ == '__main__':
    print(encode('hello'))
    print(encode('How are you today?'))
    print(decode('h2ll4'))