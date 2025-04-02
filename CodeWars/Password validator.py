# Gracida Tapia Bryan.
# 1 de Abril del 2025.

"""
Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

There needs to be at least 1 uppercase letter.
There needs to be at least 1 lowercase letter.
There needs to be at least 1 number.
The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.
"""
def password(st):
    """
    Función que verifica que una contraeña cuympla con las parametros requeridos.
    :param st: contraseña
    """
    minuscula = mayuscula = numero = caracter_especial = False  # Inicializamos las variables

    for i in st:
        if i.islower():
            minuscula = True
        if i.isupper():
            mayuscula = True
        if i.isdigit():
            numero = True
        if not i.isalnum():  # Si no es una letra ni número, es un carácter especial
            caracter_especial = True
        if minuscula == mayuscula == numero == caracter_especial:
            return True

    return False

if __name__ == '__main__':

    resultado = password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890")
    print(resultado)