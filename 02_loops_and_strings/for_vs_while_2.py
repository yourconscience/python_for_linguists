import math
n = int(input())
sum_1 = 0
binary_len = int(math.log(n, 2)) + 1
for i in range(binary_len):
    sum_1 += n % 2
    n //= 2

#####################

n = int(input())
sum_2 = 0
while n > 0:
    sum_2 += n % 2
    n //= 2

print(sum_1, sum_2)
