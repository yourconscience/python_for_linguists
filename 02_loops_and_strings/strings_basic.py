s = 'string'
l = list(s)
print(s[:3], l[:3])


#s[:3] = 'aight'
l[3:] = list('aight')
s = s[:3] + 'aight'
print(l, s)
