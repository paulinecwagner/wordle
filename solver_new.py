import numpy as np


def init():
    words = np.array([l.strip() for l in open('words')])

    counts = {}

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = 0
        for w in words:
            if letter in w:
                count += 1  # word.count(letter) # doppelte buchstaben werden nicht gezählt
        counts[letter] = count

    scores = {}
    for w in words:
        score = 0
        wordset = set(w)
        for letter in wordset:
            score += counts[letter]
        scores[w] = score

    sorted_keys = sorted(scores, key=scores.get)
    sorted_keys.reverse()
    sorted_scores = {}
    for w in sorted_keys:
        sorted_scores[w] = scores[w]

    s = list(sorted_scores.keys())

    return s


def solve(s,w,ans):
    for i in range(len(w)):
        if int(ans[i]) == 0:
            s = [x for x in s if w[i] not in x]
        elif int(ans[i]) == 1:
            s = [x for x in s if w[i] in x]
        elif int(ans[i]) == 2:
            s = [x for x in s if w[i] == x[i]]
        else:
            print('Error')
    if w in s:
        s.remove(w)
    print(s)
    return s

if __name__ == '__main__':
    sorted_words = init()

    while len(sorted_words) > 1:
        word = input('your guess: ')
        answer = input('answer: ')
        sorted_words = solve(sorted_words,word,answer)
    print('The correct solution is', sorted_words[0])


