import numpy as np
import random
from util import print_


def init():
    words = np.array([l.strip() for l in open("words")])
    sol = random.choice(words)
    return sol, words


def play(sol, w, valids):
    ans = ""
    if not w in valids:
        print_(f"{w} is not valid")
        return None
    for i in range(len(w)):
        if w[i] in sol:
            if w[i] == sol[i]:
                ans += "2"
            else:
                ans += "1"
        else:
            ans += "0"
    print_("answer: ", ans)
    return ans


if __name__ == "__main__":
    solution, valid_words = init()
    answer = ""
    count = 0
    while answer != "22222":
        word = input("your guess: ")
        answer = play(solution, word, valid_words)
        if answer is not None:
            count += 1
    print_("bing bong", word, "is correct")
    print_('this took ', count, 'guesses')

