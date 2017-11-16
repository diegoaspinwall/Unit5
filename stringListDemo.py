#Diego Aspinwall
#10-15-17
#stringListDemo.py - print out words that start with a vowel

words = input('Enter some words: ').split(' ')

for word in words:
    if word[0] in 'aeiouAEIOU':
        print(word)
