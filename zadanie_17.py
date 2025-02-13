for n in range(1, 1000):
    n_2 = bin(n)[2:]
    sum_d = n_2.count('1')

    if sum_d % 2 == 0:
        n_2 = n_2 + '0'
        n_2 = '10' + n_2[2:]
    else:
        n_2 = n_2 + '1'
        n_2 = '11' + n_2[2:]

    R = int(n_2, 2)
    if R > 40:
        print(n)
        break
