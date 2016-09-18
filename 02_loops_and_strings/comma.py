a = 1
b = 2
# ok: save one line
a, b = 1, 2
# bad: decrease readability
name, n, my_sum = input(), int(input()), 0

tmp = a
a = b
b = tmp
# great: save 2 lines & increase readability
a, b = b, a
