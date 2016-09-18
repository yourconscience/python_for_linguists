import sys

number = 23

for attempt in range(7):
    while True:
        guess = int(input('Your guess: '))
        if number == guess:
            print('Well done!')
            sys.exit(0)
        elif number < guess:
            print('Too big.')
        else:
            print('Too small.')
else:
    print('You are out of attempts')

