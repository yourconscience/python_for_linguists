number = 23
guess = 0

for attempt in range(1, 8):
    guess = int(input('Try to guess my number (' + str(attempt) + '/7): '))
    if number == guess:
        print('Well done!')
        break
    elif number < guess:
        print('My number is less than yours.')
    else:
        print('My number is greater than yours.')
else:
    print('Sorry, you are out of attempts')

