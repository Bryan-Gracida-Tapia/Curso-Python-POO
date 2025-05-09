"""
Bocce is a game played by two competing teams, with three types of balls. Each team has its own set of balls (in this kata red and black) and there is a neutral ball called the jack. The jack is thrown at the beginning of each round, followed by the players trying to throw their balls as closely to it as possible. The team with their balls closest to the jack wins the round!
The number of points the winning team scores equals the number of their balls being closer to jack than any of the other team's balls: if the red team has 3 balls closer to jack than any of the black team's balls, they will win scoring 3 points. Equidistant balls on opposing teams will cancel out and neither team will score beyond that point.
For more information on Bocce see here.
Your task
Implement a function that will return a message indicating the winner of the round. If there's no winner, return the string "No points scored".
It takes an array of balls that are hash tables (depending on your language). Each ball has 2 properties: type and distance.
The type will be "red", "black", or "jack". For all test cases, the jack will be the last element on the balls array. The distance property will be an array with two integer values. The first value is the distance thrown forward, the second value is the distance thrown left or right (negative values indicate distance to the left). For the purposes of this Kata, all balls are thrown from the same initial point.
"""

def bocce_score(balls):
    from math import dist

    jack = balls[-1]  # La ultima bola siempre sera el jack
    jack_pos = jack['distance']

    red_distances = []
    black_distances = []

    for ball in balls[:-1]:  # Excluimos el jack
        d = dist(ball['distance'], jack_pos)
        if ball['type'] == 'red':
            red_distances.append(d)
        elif ball['type'] == 'black':
            black_distances.append(d)

    red_distances.sort()
    black_distances.sort()

    if not red_distances or not black_distances:
        return "No points scored"

    if red_distances[0] < black_distances[0]:
        points = sum(1 for d in red_distances if d < black_distances[0])
        return f"red scores {points}"
    elif black_distances[0] < red_distances[0]:
        points = sum(1 for d in black_distances if d < red_distances[0])
        return f"black scores {points}"
    else:
        return "No points scored"

if __name__ == '__main__':
    print(bocce_score([
        {"type": "black", "distance": (70, -1)},
        {"type": "red", "distance": (85, -1)},
        {"type": "jack", "distance": (80, -5)}
    ]))