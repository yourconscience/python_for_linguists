def f(x):
    a = x
    global b
    b = x + 1

a, b = 0, 0
f(int(input()))
print(a, b)

