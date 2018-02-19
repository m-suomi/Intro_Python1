x = int(input('Calculate the divisors of which number? '))
a = 1
while a <= x:
    if x % a == 0:
        print (a)
        a += 1
    else:
        a += 1
