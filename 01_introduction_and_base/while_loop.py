i = 1
s = 0
while i <= 10:
    s += i
    i += 1

sudo = 'admin'
while input('Enter your login: ') != sudo:
    print('Pfff, you have no permissions, man')
print('Hello, Mr. admin, what can I do for you?')
request = input()
