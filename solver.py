import numpy as np

words = np.array([l.strip() for l in open('words')])

counts = {}

for letter in 'abcdefghijklmnopqrstuvwxyz':
    count = 0
    for word in words:
        if letter in word: count += 1 #word.count(letter) # doppelte buchstaben werden nicht gezählt
    counts[letter] = count

scores = {}
for word in words:
    score = 0
    wordset = set(word)
    for letter in wordset:
        score += counts[letter]
    scores[word] = score


sorted_keys = sorted(scores, key=scores.get)
sorted_keys.reverse()
sorted_scores = {}
for w in sorted_keys:
    sorted_scores[w] = scores[w]

sorted_words = list(sorted_scores.keys())
while len(sorted_words) > 1:
    word = input('your guess: ')
    answer = input('answer: ')
    # TODO: catch invalid inputs

    for i in range(len(word)):
        if int(answer[i]) == 0:
            sorted_words = [x for x in sorted_words if word[i] not in x]
        elif int(answer[i]) == 1:
            sorted_words = [x for x in sorted_words if word[i] in x]
        elif int(answer[i]) == 2:
            sorted_words = [x for x in sorted_words if word[i] == x[i]]
        else:
            print('Error')
    print(sorted_words)

print('The correct solution is', sorted_words[0])