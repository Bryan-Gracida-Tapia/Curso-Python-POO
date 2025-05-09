"""
Implement String#digit? (in Java StringUtils.isDigit(String)),
 which should return true if given object is a single digit (0-9), false otherwise.
"""
def is_digit(s):
    return isinstance(s, str) and len(s) == 1 and s.isdigit()
    # Verifica que la entrada sea una cadena, Asegura que es solo un caracter, verifica que sea un digito de 0 a 9


if __name__ == '__main__':
    print(is_digit(""))
    print(is_digit("7"))