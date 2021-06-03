# Series goes 2/1 * 2/3 * 4/3 * 4/5 *...... and give pi/2

import random


def wallis(n):
    product = 1
    multiplier = 2
    for n in range(n):
        odd_term = multiplier/(multiplier-1)
        even_term = multiplier/(multiplier+1)
        product = product*odd_term*even_term
        multiplier += 2

    return product*2


print("The value of pi =" + str(wallis(3000)))

# Monte carlo simulation
# Probability of falling inside is pi/4


def monte_carlo(n):
    inside_circle = 0
    inside_square = 0
    for i in range(n**2):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        distanceToOrigin = rand_x**2 + rand_y**2
        if distanceToOrigin <= 1:
            inside_circle += 1

        inside_square += 1

    ratio = inside_circle/inside_square
    return ratio*4


print(monte_carlo(1000))
