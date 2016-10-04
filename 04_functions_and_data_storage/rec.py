import time

def count_to_start(seconds):
    if seconds == 0:
        print('Start!')
    else:
        print(str(seconds) + ' seconds to start...')
        time.sleep(1)
        count_to_start(seconds - 1)

count_to_start(10)
