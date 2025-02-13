# если сумма цифр в двоичной записи
for n in range(28, 100):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = "11" + b[2:] + '1'
    r = int(b, 2)
    print(n, r)
