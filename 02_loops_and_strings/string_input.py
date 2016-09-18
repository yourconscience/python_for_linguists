# Read multiple lines
n = int(input())
lines = []
for i in range(n):
    lines.append(input())
text = ' '.join(lines)
words = text.split()
print(words)


