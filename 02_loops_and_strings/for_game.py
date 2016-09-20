number = 23
guess = 0

for attempt in range(1, 8):
    guess = int(input('Your guess ({}/7): '.format(str(attempt))))
    if number == guess:
        print('Well done!')
        break
    elif number < guess:
        print('Too big.')
    else:
        print('Too small.')
else:
    print('You are out of attempts')

