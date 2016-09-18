number = 23
cnt = 0

while True:
    guess = int(input('Your guess: '))
    if not (0 <= guess < 100):
        print('It is from 0 to 100.')
        continue
    if number == guess:
        print('Well done!')
        print(cnt + 1, 'trials')
        break
    elif number < guess:
        print('Too big.')
        cnt += 1
    else:
        print('Too small.')
        cnt += 1

