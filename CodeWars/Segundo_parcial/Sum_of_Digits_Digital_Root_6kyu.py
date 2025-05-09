"""
Digital root is the recursive sum of all the digits in a number.

Given , take the sum of the digits of . If that value has more
than one digit, continue reducing in this way until a single-digit
number is produced. The input will be a non-negative integer.nn
"""
def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(int(digit) for digit in str(n)))

if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(965))
    print(digital_root(6))