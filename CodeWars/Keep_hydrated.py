"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
"""
def litres(time):
    return time // 2





if __name__ == '__main__':
    result = litres(0)
    print(result)
    result = litres(4)
    print(result)
    result = litres(5)
    print(result)
    result = litres(12)
    print(result)
    result = litres(1.4)
    print(result)