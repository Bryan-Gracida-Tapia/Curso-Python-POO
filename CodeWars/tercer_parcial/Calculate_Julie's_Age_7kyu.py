""""
Julie is x years older than her brother, and she is also y times as old as him.

Given x and y, create a function calculating Julie's age.

For example:

x: 6
y: 3
output: 9
Note also that x can be negative, and y can be a decimal.

x: -15,
y: 0.25
output: 5
That is, Julie is 15 years younger and 0.25 times the age of her brother.

Do not concern yourself with the imperfections inherent in dividing by floating point numbers, as your answer will have a tolerance of 1e-9. Also, for the sake of simplicity, Julie is never the same age as her brother.
"""
def age(x: float, y: float) -> float:
    # Calculamos la edad del hermano y luego la de Julie
    brother = x / (y - 1)
    julie = brother + x
    return julie

if __name__ == '__main__':
    print(age(-15, 0.25))
    print(age(6, 3))