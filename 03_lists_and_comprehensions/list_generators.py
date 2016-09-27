zeroes = [0, 0, 0, 0, 0]
zeroes = [0] * 5
zeroes = [0 for i in range(5)]
squares = [i * i for i in range(5)]
str_squares = ' '.join([str(i) for i in squares])
print(str_squares)

ints = [int(i) for i in input().split()]
print(sum(ints))
