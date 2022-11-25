import itertools
import random

inp = input('''==Który podpunkt z zadania 7.6 chcesz uruchomić==
==Do wyboru : a, b, c==
''')

if (inp == 'a') or (inp == 'A'):
    while True:
        it = itertools.cycle(range(0, 2))
        print(next(it))
        print(next(it))

if (inp == 'b') or (inp == 'B'):
    while True:
        it = itertools.cycle(random.choice(["A", "B", "C", "D"]))
        print(next(it))

if (inp == 'c') or (inp == 'C'):
    while True:
        it = itertools.cycle(range(0, 7))
        for i in range(7):
            print(next(it))
