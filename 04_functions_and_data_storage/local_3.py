def f(x):
    global b
    print(b)
    b = x
    return x

b = 0
print(f(1))
print(b)


