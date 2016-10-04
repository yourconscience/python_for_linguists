def list_range(start, stop=None, step=1):
    if stop == None:
        start, stop = 0, start
    res = []
    while start < stop:
        res.append(start)
        start += step
    return res

print(list_range(5 ,10))
print(list_range(10, step=2))
