#Diego Aspinwall
#10-13-17
#middleWord.py

words = input('Enter words: ').split(' ')

print(words[len(words)/2])
if len(words)%2 != 0:
    print(words[(len(words)/2)-1])
