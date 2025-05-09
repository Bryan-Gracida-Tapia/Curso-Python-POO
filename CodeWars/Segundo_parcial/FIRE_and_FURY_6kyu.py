"""
He is not very happy.

The only letters still working are uppercase E, F, I, R, U, Y.

An angry tweet is sent to the department responsible for presidential phone maintenance.

Kata Task
Decipher the tweet by looking for words with known meanings.

FIRE = "You are fired!"
FURY = "I am furious."
If no known words are found, or unexpected letters are encountered, then it must be a "Fake tweet."

Notes
The tweet reads left-to-right.
Any letters not spelling words FIRE or FURY are just ignored
If multiple of the same words are found in a row then plural rules apply -
FIRE x 1 = "You are fired!"
FIRE x 2 = "You and you are fired!"
FIRE x 3 = "You and you and you are fired!"
etc...
FURY x 1 = "I am furious."
FURY x 2 = "I am really furious."
FURY x 3 = "I am really really furious."
etc...
Examples
ex1. FURYYYFIREYYFIRE = "I am furious. You and you are fired!"
ex2. FIREYYFURYYFURYYFURRYFIRE = "You are fired! I am really furious. You are fired!"
ex3. FYRYFIRUFIRUFURE = "Fake tweet."
"""

def fire_and_fury(tweet):
    import re       # se utiliza para buscar, verificar, o reemplazar patrones de texto.

    if re.search(r'[^EFIRUY]', tweet):  # Busca si existe al menos una coincidencia del patrón en el texto. | Devuelve un objeto si encuentra algo. | Devuelve None si no encuentra nada.
        return "Fake tweet."

    # Find all FIRE and FURY in order
    words = re.findall(r'(FIRE|FURY)', tweet)   # Devuelve todas las coincidencias.

    if not words:
        return "Fake tweet."

    result = []
    i = 0
    while i < len(words):
        word = words[i]
        count = 1
        while (i + 1 < len(words)) and (words[i + 1] == word):
            count += 1
            i += 1

        if word == "FIRE":
            result.append("You" + " and you" * (count - 1) + " are fired!")
        elif word == "FURY":
            result.append("I am" + " really" * (count - 1) + " furious.")
        i += 1

    return " ".join(result) # Unimos todas las frases traducidas con espacios y las retornamos