a = (1, 2, 3)
b = tuple() # b = ()
c = (3,) # comma is required

l = [0, 1, 2, 6, 4, 5]
t = tuple(l)
print(t[0], t[-2:])
l[3] = 3
t[3] = 3 # error
