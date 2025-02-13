def expr(x, A):
    xinP = 15 <= x <= 40
    xinQ = 21 <= x <= 63
    xinA = A[0] <= x <= A[1]
    return xinP <= ((xinQ and (not xinA)) <= (not xinP))

A = [0, 100]
while all(expr(x, A) for x in range(0, 100)):
    A[0] += 1
A[0] -= 1
while all(expr(x, A) for x in range(0, 100)):
    A[1] -= 1
A[1] += 1
