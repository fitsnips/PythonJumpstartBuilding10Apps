# classic
from time import sleep


def fibonacci(limit):

    numbers = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        numbers.append(current)

    return numbers


for n in fibonacci(10000000000):
    print(n, end=', ')


print()
# generator

def fibonacci_co():

    current = 0
    next = 1

    #sleep(1)
    while True:
        current, next = next, next + current
        yield current


for n in fibonacci_co():
    if n > 10000000000:
        break

    print(n, end=', ')