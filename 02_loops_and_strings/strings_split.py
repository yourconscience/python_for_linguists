sent = 'fall leaves as soon as leaves fall'
words = sent.split()
words = words[::-1]
sent = ' '.join(words)
print(sent)

nums = '1,2,3,4'
print('\n'.join(nums.split(',')))
