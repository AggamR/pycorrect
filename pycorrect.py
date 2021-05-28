# See the "LICENSE" file for licensing information

from math import sqrt

def dist2d(item1, item2, array):
    # coors of items
    i1 = []
    i2 = []

    # find it in array
    for x in range(len(array)):
        for y in range(len(array[x])):
            if type(array[x][y]) == str:
                if array[x][y] == item1:
                    i1 = [x, y]
                elif array[x][y] == item2:
                    i2 = [x, y]
            elif type(array[x][y]) == list:
                for i in range(len(array[x][y])):
                    if array[x][y][i] == item1:
                        i1 = [x, y]
                    elif array[x][y][i] == item2:
                        i2 = [x, y]
    
    return sqrt( (i2[0] - i1[0])**2 + (i2[1] - i1[1])**2 )


def correct(word, bank):
    #if word in bank: return word
    
    keys = [
            list('qwertyuiop[]'),
            list('asdfghjkl;\''),
            [list('zxcvbnm,.'), ['/', '?']]
    ]
    
    print(keys)

    score = 0.0
    bestScore = 0.0
    bestWord = ''
    d = 0

    for poss in bank:
        score = 0
        for i in range(len(word)):
            for j in range(int((i+1) / 2)):
                try:
                    if word[i+j] == poss[i+j]:
                        score += (i-j)                 
                except:
                    next
                
                try:
                    d = 1 / dist2d(word[i+j], poss[i+j], keys)
                    score += d
                except:
                    next
        
        if score > bestScore:
            bestScore = score
            bestWord = poss
    
        print(f'{poss}: {score}')

    return bestWord


# The following code is for testing purposes. 
bank = ['bruh', 'bru', 'bra?', 'bra/']  # bank of possible words to mach for
word = 'bruy'  # "the typo"

print(correct(word, bank))