import solver as s
import game as g


def game(solution):
    count = 0
    sorted_words = s.init()
    answer = ''
    while answer != '22222':
        count += 1
        word, answer = g.play(solution, sorted_words[0])
        sorted_words = s.solve(sorted_words, word, answer)
    print('bing bong', word, 'is correct')
    print('this took ', count, 'guesses')
    return word, count

def how_many_guesses():
    sorted_words = s.init()
    hmg = {}
    for element in sorted_words:
        print('##### ', element)
        word, count = game(element)
        hmg[word] = count

    sorted_keys_hmg = sorted(hmg, key=hmg.get)
    sorted_keys_hmg.reverse()
    sorted_hmg = {}
    for w in sorted_keys_hmg:
        sorted_hmg[w] = hmg[w]
    f = open("how_many_guesses.txt", "w")
    for so in sorted_hmg:
        f.write(so + '   -   ' + str(sorted_hmg[so]) + '\n')
    f.close()
    return sorted_hmg

if __name__ == '__main__':
    #game(g.init())
    #game('react')
    print(how_many_guesses())
    # alter alert (later)
    # saner (snare)
    # react (trace)
    #




