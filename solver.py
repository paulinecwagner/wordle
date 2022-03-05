import numpy as np
from  util import print_

def init():
    words = np.array([l.strip() for l in open('words')])

    counts = {}

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = 0
        for w in words:
            count += w.count(letter)
            #if letter in w:
                #count += 1  # w.count(letter) # doppelte buchstaben werden nicht gezählt
        counts[letter] = count

    scores = {}
    for w in words:
        score = 0
        wordset = set(w)
        for letter in wordset:
            score += counts[letter]
        score += len(wordset)*10000
        scores[w] = score

    sorted_keys = sorted(scores, key=scores.get)
    sorted_keys.reverse()

    return sorted_keys


def solve(s,w,ans):
    for i in range(len(w)):
        if int(ans[i]) == 0:
            s = [x for x in s if w[i] not in x]
        elif int(ans[i]) == 1:
            s = [x for x in s if w[i] in x and w[i]!=x[i]]
        elif int(ans[i]) == 2:
            s = [x for x in s if w[i] == x[i]]
        else:
            print_('Error')
    if ans!='22222':
        if not s:
            raise ValueError('No solution')
        print_(s)
        print_('Your next guess should be:', s[0])
    return s

def check(ans):
    if len(ans) != 5:
        return False
    l=[]
    for a in ans:
        l.append(int(a) == 0 or int(a) == 1 or int(a) == 2 )
    return all(l)


def main():
    sorted_words = init()

    while len(sorted_words) > 1:
        # check for invalid inputs
        while True:
            word = input('your guess: ')
            if word in sorted_words:
                break
            print_('invalid input')
        while True:
            answer = input('answer: ')
            if check(answer):
                break
            print_('invalid input')

        sorted_words = solve(sorted_words,word,answer)

    print_('The correct solution is', sorted_words[0])


if __name__ == '__main__':
    main()
