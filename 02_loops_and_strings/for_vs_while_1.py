n = 10
sum_1 = 0
for i in range(n + 1):
    sum_1 += i * i

sum_2 = 0
i = 0
while i <= n:
    sum_2 += i * i
    i += 1

print(sum_1, sum_2)
