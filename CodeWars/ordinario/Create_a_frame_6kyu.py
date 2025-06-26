"""
Given an array of strings and a character to be used as border, output the frame with the content inside.

Notes:

Always keep a space between the input string and the left and right borders.
The biggest string inside the array should always fit in the frame.
The input array is never empty.
"""

def frame(text, char):
    ########
    # your #
    # code #
    # here #
    ########
    num_max = max(len(word) for word in text)

    result = ''
    salto = '\n'
    result += char * (num_max + 4) + salto

    for word in text:
        result += f"{char} {word.ljust(num_max)} {char}\n"

    result += char * (num_max + 4)

    return result

if __name__ == '__main__':
    frame(['Small', 'frame','wer','oil'], '~')