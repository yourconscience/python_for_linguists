def max(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    return res

print(max(3, 5, 4))
