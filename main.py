import numpy as np

words = np.array([l.strip() for l in open('words')])

counts = {}

for letter in 'abcdefghijklmnopqrstuvwxyz':
    count = 0
    for word in words:
        if letter in word: count += 1 #word.count(letter) # doppelte buchstaben werden nicht gezählt
    counts[letter] = count

print(counts)


scores = {}
for word in words:
    score = 0
    wordset = set(word)
    for letter in wordset:
        score += counts[letter]
    scores[word] = score

print(scores)

sorted_keys = sorted(scores, key=scores.get)
sorted_keys.reverse()
sorted_scores = {}
for w in sorted_keys:
    sorted_scores[w] = scores[w]
print(sorted_scores)


f = open("best_words.txt", "w")
for s in sorted_scores:
    f.write(s + '   -   ' + str(sorted_scores[s]) + ' \n')
f.close()

sorted_words = list(sorted_scores.keys())
mvp = [sorted_words[0]]
used = sorted_words[0]

for w in sorted_words:
    if len(set(w).symmetric_difference(set(used))) == len(w) + len(used):
        mvp.append(w)
        used += w

print(mvp)


x = set('later')
z=['later']
for w in sorted_words:
    c = 0
    for y in x:
        if y in w:
            c+=1
    if c == 0:
        x.update(set(w))
        print(x)
        z.append(w)

print('2nd try', z)

print(sorted_scores['pudgy'])