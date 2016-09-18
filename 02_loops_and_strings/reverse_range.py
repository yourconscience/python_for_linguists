n = int(input())
mystery_sum = 0
for i in range(n, 0, -1):
    if mystery_sum % i == 0:
        mystery_sum += i
print(mystery_sum)
