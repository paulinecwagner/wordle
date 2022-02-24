import numpy as np
import random


def init():
    words = np.array([l.strip() for l in open('words')])
    sol = random.choice(words)
    return sol


def play(sol,w):

    ans = ''
    for i in range(len(w)):
        if w[i] in sol:
            if w[i] == sol[i]:
                ans += '2'
            else:
                ans += '1'
        else:
            ans += '0'
    print('answer: ', ans)
    return w, ans



if __name__ == '__main__':
    solution = init()
    answer = ''
    while answer != '22222':
        word = input('your guess: ')
        word, answer = play(solution,word)
    print('bing bong', word, 'is correct')
