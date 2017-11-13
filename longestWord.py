#Diego Aspinwall
#10-13-17
#longestWord.py

words = input('Enter darn words BOI: ').split(' ')

l = 0
for w in words:
    if l < len(w):
        l = len(w)
print(w)
