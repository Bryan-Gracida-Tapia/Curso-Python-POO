""""
The Hamming weight of a string is the number of symbols that are different from the zero-symbol of the alphabet used. There are several algorithms for efficient computing of the Hamming weight for numbers. In this Kata, speaking technically, you have to find out the number of '1' bits in a binary representation of a number. Thus,

hamming_weight(10) # 1010  => 2
hamming_weight(21) # 10101 => 3
The interesting part of this task is that you have to do it without string operation (hey, it's not really interesting otherwise)

;)
"""
def hamming_weight(n: int) -> int:
    count = 0
    while n > 0:
        # Incrementamos count si el bit menos significativo es 1
        count += n & 1
        # Desplazamos n un bit a la derecha para revisar el siguiente bit
        n >>= 1
    return count

if __name__ == '__main__':
    print(hamming_weight(10))
    print(hamming_weight(21))