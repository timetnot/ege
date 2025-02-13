from itertools import *

t = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
g = 'ab ba af fa bc cb ca ac ec ce ed de eg ge df fd dg gd'

for per in permutations('abcdefg'):
    new_g = t
    for i in range(1, 8):
        new_g = new_g.replace(str(i), per[i - 1])
    if set(new_g.split()) == set(g.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
