"""
Mutual Recursion allows us to take the fun of regular recursion (where a function calls
itself until a terminating condition) and apply it to multiple functions calling each other!

Let's use the Hofstadter Female and Male sequences to demonstrate this technique.
You'll want to create two functions F and M such that the following equations are true:

F(0) = 1
M(0) = 0
F(n) = n - M(F(n - 1))
M(n) = n - F(M(n - 1))
Don't worry about negative numbers, n will always be greater than or equal to zero
"""
def f(n):
    if n == 0:
        return 1
    return n - m(f(n - 1))

def m(n):
    if n == 0:
        return 0
    return n - f(m(n - 1))

if __name__ == '__main__':
    print(f(5))