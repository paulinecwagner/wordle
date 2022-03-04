import solver as s
import game as g
from datetime import datetime


def game(solution):
    count = 0
    sorted_words = s.init()
    answer = ''
    while answer != '22222':
        count += 1
        guess = sorted_words[0]
        answer = g.play(solution, guess)
        sorted_words = s.solve(sorted_words, guess, answer)
    print('bing bong', guess, 'is correct')
    print('this took ', count, 'guesses')
    return guess, count

def how_many_guesses():
    sorted_words = s.init()
    hmg = {}
    for element in sorted_words:
        print('##### ', element)
        word, count = game(element)
        hmg[word] = count

    avg_guesses = sum(hmg.values())/len(hmg.values())
    max_guesses = max(hmg.values())

    g = open('stats.txt', 'a')
    stat = ' - average:' + str(avg_guesses) + ' / maximum:'+ str(max_guesses)
    g.write(datetime.now(), stat)


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
    print(how_many_guesses())

if __name__ == '__main__':
    main()




