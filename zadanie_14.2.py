x = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
c = 0
while x > 0:
   if x % 25 == 0:
      c += 1
   x //= 25
print(c) 
