def gcd(a, b):
    '''Returns greatest common divisor of natural numbers a and b. '''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(2, 1))
print(gcd(8, 12))
