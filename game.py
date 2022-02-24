import numpy as np
import random

words = np.array([l.strip() for l in open('words')])

solution = random.choice(words)
answer = ''
while answer != '22222':
    answer = ''
    word = input('your guess: ')
    if len(word) != 5:
        print('word must have 5 letters')
        continue
    if word not in words:
        print('invalid word')
        continue
    for i in range(len(word)):
        if word[i] in solution:
            if word[i] == solution[i]:
                answer += '2'
            else:
                answer += '1'
        else:
            answer += '0'

    print('answer: ', answer)

print('bing bong', word,'is correct')