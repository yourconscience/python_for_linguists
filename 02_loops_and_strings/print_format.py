s1 = 'abc123_&'
s2 = 'Привет, мир'
s3 = "I'm hungry and you\'re not"

print(s1, '\n', s2, '\n', s3)

print(s1 + '\n' + s2 + '\n' + s3)

print(s1, s2, s3, sep='\n')

print(s1, s2, s3, sep='\t', end='\n')

print('{}\t{}\t{}\n'.format(s1, s2, s3))
print('{s1}\t{hello}\t{hungry}\n'.format(s1=s1, hello=s2, hungry=s3))
