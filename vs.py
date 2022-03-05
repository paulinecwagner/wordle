import solver as s
import game as g
from datetime import datetime
from copy import copy
from util import print_

def game(solution):
    count = 0
    sorted_words = s.init()
    all_words = copy(sorted_words)
    answer = ''
    while answer != '22222':
        count += 1
        guess = sorted_words[0]
        answer = g.play(solution, guess, all_words)
        sorted_words = s.solve(sorted_words, guess, answer)
    print_('bing bong', guess, 'is correct')
    print_('this took ', count, 'guesses')
    return guess, count

def how_many_guesses():
    sorted_words = s.init()
    hmg = {}
    for element in sorted_words:
        print_('##### ', element)
        word, count = game(element)
        hmg[word] = count

    avg_guesses = sum(hmg.values())/len(hmg.values())
    max_guesses = max(hmg.values())

    g = open('stats.txt', 'a')
    stat = ' - average:' + str(avg_guesses) + ' / maximum:'+ str(max_guesses)
    g.write(str(datetime.now())+ str(stat)+'\n')


    '''sorted_keys_hmg = sorted(hmg, key=hmg.get)
    sorted_keys_hmg.reverse()
    sorted_hmg = {}
    for w in sorted_keys_hmg:
        sorted_hmg[w] = hmg[w]
    f = open("how_many_guesses.txt", "w")
    for so in sorted_hmg:
        f.write(so + '   -   ' + str(sorted_hmg[so]) + '\n')
    f.close()'''

    return stat

def main():
    #game(g.init())
    #game('giant')

    start = datetime.now()
    print_(how_many_guesses())
    finish = datetime.now()
    print(f"runtime: {finish - start}")

if __name__ == '__main__':
    main()




