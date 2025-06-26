"""
Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.

Example (input -> output):
'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'
You can learn more about Base64 encoding and decoding here.

Note: This kata uses the non-padding version ("=" is not added to the end).


"""

from base64_5kyu

def to_base_64(s):
    encoded = b64encode(s.encode('ascii')).decode('ascii')
    return encoded.rstrip('=')

def from_base_64(s):
    padding = '=' * (-len(s) % 4)
    decoded = b64decode(s + padding).decode('ascii')
    return decoded





if __name__ == '__main__':
    print(to_base_64('this is a string!!'))
    print(from_base_64('dGhpcyBpcyBhIHN0cmluZyEh'))